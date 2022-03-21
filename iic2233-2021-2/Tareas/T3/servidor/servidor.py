import json
import socket
import threading
import random

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


class Servidor:
    _id_cliente = 1

    def __init__(self, host, port):
        print("Inicializando servidor...")

        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Clientes actualmente conectados al servidor
        self.clientes_conectados = {}
        self.lock_archivos = threading.Lock()
        self.jugadores = {}  # llaves: nombre, valores: socket
        self.nombres_jugadores = {}  # llaves: id, valores: nombre
        self.estado_jugadores = {}  # llaves: nombre, valores: en que ventana están
        self.unir_y_escuchar()

    def unir_y_escuchar(self):
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        print('host, port: ', (self.host, self.port))
        self.aceptar_conexiones()

    def aceptar_conexiones(self):
        my_thread = threading.Thread(target=self.thread_aceptar_conexiones)
        my_thread.start()

    def thread_aceptar_conexiones(self):
        while True:
            try:
                socket_cliente, address = self.socket_servidor.accept()
                print("\nConexión aceptada desde", address)
                self.clientes_conectados[Servidor._id_cliente] = socket_cliente
                thread_cliente = threading.Thread(target=self.thread_escuchar_cliente,
                                                  kwargs={"socket_cliente": socket_cliente,
                                                          "id_cliente": Servidor._id_cliente})
                Servidor._id_cliente += 1
                thread_cliente.start()

                self.enviar("Gracias por conectarte\n", socket_cliente)
            except ConnectionError:
                # print("Ocurrió un error.")
                break

    def thread_escuchar_cliente(self, socket_cliente, id_cliente):
        while True:
            try:
                mensaje = self.recibir_mensaje(socket_cliente)
                if not mensaje:
                    raise ConnectionError
                respuesta = self.manejar_comando(mensaje, socket_cliente, id_cliente)
                if not respuesta:
                    raise ConnectionError
                self.enviar(respuesta, socket_cliente)
            except ConnectionError:
                print("Ocurrió un error.")
                socket_cliente.close()
                break

    def recibir_mensaje(self, socket_cliente):
        longitud_bytes_de_respuesta = socket_cliente.recv(4)
        longitud_respuesta = int.from_bytes(
            longitud_bytes_de_respuesta, byteorder='big')
        respuesta = bytearray()

        while len(respuesta) < longitud_respuesta:
            leer_longitud = min(4096, longitud_respuesta - len(respuesta))
            respuesta.extend(socket_cliente.recv(leer_longitud))
        return self.decodificar_mensaje(respuesta)

    def enviar(self, mensaje, sock_cliente):
        mensaje_codificado = self.codificar_mensaje(mensaje)
        longitud_bytes_mensaje = len(mensaje_codificado).to_bytes(4, byteorder='big')
        sock_cliente.sendall(longitud_bytes_mensaje + mensaje_codificado)

    def recibir_mensaje2(self, socket_cliente):
        longitud_bytes_de_respuesta = socket_cliente.recv(4)
        longitud_respuesta = int.from_bytes(
            longitud_bytes_de_respuesta, byteorder='little')
        respuesta = bytearray()
        while len(respuesta) < longitud_respuesta:
            bytes_numero_bloque = socket_cliente.recv(4)
            numero_bloque = int.from_bytes(
                bytes_numero_bloque, byteorder='big')
            leer_longitud = min(80, longitud_respuesta - len(respuesta))
            respuesta.extend(socket_cliente.recv(leer_longitud))
        if not self.decodificar_mensaje(respuesta):
            print(longitud_respuesta)
            print(respuesta)
        return self.decodificar_mensaje(respuesta)

    def enviar2(self, msg, socket_cliente):
        mensaje_codificado = self.codificar_mensaje(msg)
        longitud_bytes_mensaje = len(mensaje_codificado).to_bytes(4, byteorder='little')
        enviar_msg = longitud_bytes_mensaje
        tamano_bloque = 80
        for i in range(0, len(mensaje_codificado), tamano_bloque):
            numero_bloque = i // tamano_bloque
            bytes_numero_bloque = numero_bloque.to_bytes(4, byteorder='big')
            enviar_msg += bytes_numero_bloque
            men = mensaje_codificado[i:i + tamano_bloque]
            while len(men) < tamano_bloque:
                men += b'\x00'
            enviar_msg += men
        socket_cliente.sendall(enviar_msg)

    def manejar_comando(self, recibido, socket_cliente, id_cliente):
        respuesta = {}
        if 'validacion' in recibido:
            print('Verificando usuario')
            nombre = recibido['validacion']['nombre']
            fecha = recibido['validacion']['fecha']
            credenciales_correctas = False
            usuario_unico = False
            if nombre not in self.jugadores:
                usuario_unico = True
            if p['min_caract'] <= len(nombre) <= p['max_caract'] and nombre.isalnum():
                f = fecha.split('/')
                if len(f) == 3:
                    try:
                        if 1 <= int(f[0]) <= 31 and 1 <= int(f[1]) <= 12 and \
                                p['ano_minimo'] <= int(f[2]) <= p['ano_maximo']:
                            credenciales_correctas = True
                    except ValueError:
                        credenciales_correctas = False
            if len(self.jugadores) >= p['capacidad_servidor']:  # Servidor lleno
                servidor_disponible = False
                print('Servidor lleno, no se aceptan nuevos jugadores.')
            else:
                servidor_disponible = True
            if all([credenciales_correctas, usuario_unico, servidor_disponible]):
                print('Usuario válido')
                respuesta['nombre'] = nombre
                self.jugadores[nombre] = socket_cliente
                self.nombres_jugadores[id_cliente] = nombre
                self.estado_jugadores[nombre] = {'estado': 'sala_principal'}
            else:
                print('Usuario inválido')
            respuesta['credenciales'] = {'formato': credenciales_correctas,
                                         'no_repetido': usuario_unico,
                                         'servidor_disponible': servidor_disponible}
        if 'retar' in recibido:
            retador = recibido['retar']['retador']
            retado = recibido['retar']['retado']
            print(f'{retador} ha retado a {retado} a jugar.')
            self.estado_jugadores[retador] = {'estado': 'reto'}
            self.estado_jugadores[retado] = {'estado': 'reto'}
            respuesta['retar'] = recibido['retar']
            socket_rival = self.jugadores[retado]
            resp = {}
            resp['retado'] = recibido['retar']
            self.enviar(resp, socket_rival)

        if 'respuesta_reto' in recibido:
            rival = recibido['respuesta_reto']['retador']
            player = recibido['respuesta_reto']['retado']
            answer = recibido['respuesta_reto']['respuesta']
            if answer:
                self.estado_jugadores[rival] = {'estado': 'jugando'}
                self.estado_jugadores[player] = {'estado': 'jugando'}
                primero = random.choice([player, rival])
                print()
                print(f'{player} se enfrentará a {rival}')
                print(f'Por sorteo, parte apostando {primero}')
                print()
                turno_r = True if primero == rival else False
                turno_p = not turno_r
            else:
                turno_r = None
                turno_p = None
                self.estado_jugadores[rival] = {'estado': 'sala_principal'}
                self.estado_jugadores[player] = {'estado': 'sala_principal'}
            resp = {}
            resp['juego'] = [rival, player, answer, turno_r]
            respuesta['juego'] = [player, rival, answer, turno_p]
            socket_rival = self.jugadores[rival]
            self.enviar(resp, socket_rival)

        if 'apuesta_realizada' in recibido:
            rival = recibido['apuesta_realizada']['rival']
            nom = recibido["apuesta_realizada"]["nombre"]
            cant_apuesta = recibido["apuesta_realizada"]['cantidad_apostada']
            if 'paridad_oponente' in recibido['apuesta_realizada']:
                paridad = recibido["apuesta_realizada"]['paridad_oponente']
                print(f'{nom} ha apostado {cant_apuesta} que {rival} puso una cantidad {paridad}')
            else:
                print(f'{nom} ha apostado {cant_apuesta} canicas.')
                print(f'En la siguiente ronda es el turno de {nom}')
            resp = {}
            resp['apuesta_rival'] = recibido['apuesta_realizada']
            socket_rival = self.jugadores[rival]
            self.enviar(resp, socket_rival)

        if 'cheatcode' in recibido:
            rival = recibido['cheatcode']['rival']
            resp = {}
            resp['cheated'] = recibido['cheatcode']
            socket_rival = self.jugadores[rival]
            self.enviar(resp, socket_rival)

        if 'derrota' in recibido or 'victoria' in recibido:
            if 'derrota' in recibido:
                resultado = 'derrota'
                resultandont = 'victoria'
            else:
                resultado = 'victoria'
                resultandont = 'derrota'
            loser = recibido[resultado]['nombre']
            victorioso = recibido[resultado]['rival']
            razon = recibido[resultado]['razon']
            print(f'¡{loser} a conseguida la {resultado} frente a {victorioso}!')
            resp = {}
            resp[resultandont] = {'nombre': victorioso, 'rival': loser, 'razon': razon}
            respuesta[resultado] = {'nombre': loser, 'rival': victorioso, 'razon': razon}
            socket_victorioso = False
            try:
                del self.estado_jugadores[loser]
                del self.estado_jugadores[victorioso]
                socket_victorioso = self.jugadores[victorioso]
                self.jugadores.pop(loser)
                id_a_eliminar = -1
                for i, n in self.nombres_jugadores.items():
                    if n == loser:
                        id_a_eliminar = i
                        break
                self.nombres_jugadores.pop(id_a_eliminar)

                self.jugadores.pop(victorioso)
                id_a_eliminar = -1
                for i, n in self.nombres_jugadores.items():
                    if n == victorioso:
                        id_a_eliminar = i
                        break
                self.nombres_jugadores.pop(id_a_eliminar)
            except KeyError:
                if 'victoria' in resp:
                    del resp['victoria']
                if 'victoria' in respuesta:
                    del respuesta['victoria']
                resp['derrota'] = {'nombre': victorioso, 'rival': loser, 'razon': razon}
                respuesta['derrota'] = {'nombre': loser, 'rival': victorioso, 'razon': razon}
            if socket_victorioso:
                self.enviar(resp, socket_victorioso)

        if 'desconectar' in recibido:
            nombre = recibido['desconectar']
            try:
                del self.estado_jugadores[nombre]
                self.jugadores.pop(nombre)
                id_a_eliminar = -1
                for i, n in self.nombres_jugadores.items():
                    if n == nombre:
                        id_a_eliminar = i
                        break
                self.nombres_jugadores.pop(id_a_eliminar)
            except KeyError:
                pass
            respuesta['desconectar'] = True
        respuesta['jugadores'] = list(self.jugadores)
        respuesta['estado_jugadores'] = self.estado_jugadores
        return respuesta

    @staticmethod
    def codificar_mensaje(mensaje):
        """
        Serializa el mensaje a enviar a un json.
        """
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode(encoding='utf-8')

            a = mensaje_bytes[::3]
            b = mensaje_bytes[1::3]
            c = mensaje_bytes[2::3]

            if b[0] > c[0]:
                aux = bytearray()
                for i in range(0, len(mensaje_bytes), 1):
                    # Aqui obtenemos nuestro chunk
                    chunk = bytearray(mensaje_bytes[i:i + 1])
                    if chunk == b"\x03":
                        aux.extend(b"\x05")
                    elif chunk == b"\x05":
                        aux.extend(b"\x03")
                    else:
                        aux.extend(chunk)
                A = aux[::3]
                B = aux[1::3]
                C = aux[2::3]
                res = bytearray(A + B + C + b"\x00")
            else:
                A = mensaje_bytes[::3]
                B = mensaje_bytes[1::3]
                C = mensaje_bytes[2::3]
                res = bytearray(B + A + C + b"\x01")
            return res
        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje.')

    @staticmethod
    def decodificar_mensaje(msg_bytes):
        """
        Deserializa los bytes recibidos, devolviendo un diccionario a partir
        del json procesado.
        """
        try:
            res = bytearray(msg_bytes)
            if res[-1] == 0:
                aux = bytearray()
                for i in range(0, len(res) - 1, 1):
                    # Aqui obtenemos nuestro chunk
                    chunk = bytearray(res[i:i + 1])
                    if chunk == b"\x03":
                        aux.extend(b"\x05")
                    elif chunk == b"\x05":
                        aux.extend(b"\x03")
                    else:
                        aux.extend(chunk)

                len_a = len(aux) // 3 + 1
                len_b = len(aux) // 3 + 1 if len(aux) % 3 != 1 else len(aux) // 3
                len_c = len(aux) // 3 + 1 if len(aux) % 3 == 0 else len(aux) // 3
                A = aux[:len_a]
                B = aux[len_a:len_a + len_b]
                C = aux[len_a + len_b:len_a + len_b + len_c]
                decriptado = bytearray()
                for i in range(0, len_a, 1):
                    chunk_a = bytearray(A[i:i + 1])
                    decriptado.extend(chunk_a)
                    chunk_b = bytearray(B[i:i + 1])
                    decriptado.extend(chunk_b)
                    chunk_c = bytearray(C[i:i + 1])
                    decriptado.extend(chunk_c)
            else:
                aux = res[:-1]
                len_a = len(aux) // 3 + 1 if len(aux) % 3 != 0 else len(aux) // 3
                len_b = len_a if len(aux) % 3 != 1 else len_a - 1
                len_c = len_a if len(aux) % 3 == 0 else len_a - 1
                B = aux[:len_b]
                A = aux[len_b:len_b + len_a]
                C = aux[len_b + len_a:len_b + len_a + len_c]
                decriptado = bytearray()
                for i in range(0, len_a, 1):
                    chunk_a = bytearray(A[i:i + 1])
                    decriptado.extend(chunk_a)
                    chunk_b = bytearray(B[i:i + 1])
                    decriptado.extend(chunk_b)
                    chunk_c = bytearray(C[i:i + 1])
                    decriptado.extend(chunk_c)
            mensaje = json.loads(decriptado)
            return mensaje
        except json.JSONDecodeError:
            print('No se pudo decodificar el mensaje.')
            return dict()
