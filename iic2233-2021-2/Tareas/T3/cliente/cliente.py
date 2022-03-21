import json
import socket
import threading
from PyQt5.QtCore import QObject, pyqtSignal


class Cliente(QObject):
    senal_credenciales = pyqtSignal(dict)
    senal_actualizar_principal = pyqtSignal(dict)
    senal_cliente_desconectado = pyqtSignal(str)
    senal_reto_aceptado = pyqtSignal(dict)
    senal_reto_rechazado = pyqtSignal(dict)
    senal_juego_terminado = pyqtSignal(dict)
    senal_cheated = pyqtSignal(dict)
    senal_apuesta_rival = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.nombre = ''
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.evento_prints = threading.Event()
        self.evento_prints.set()

        try:
            self.conectar_al_servidor()
            self.escuchar()
            # self.recibir_input()
        except ConnectionError:
            self.salir()

    def conectar_al_servidor(self):
        self.socket_cliente.connect((self.host, self.port))
        print("El cliente se ha conectado exitosamente al servidor")

    def escuchar(self):
        my_thread = threading.Thread(target=self.thread_escuchar)
        my_thread.start()

    def thread_escuchar(self):
        while True:
            try:
                self.enviar({'update': 'ping'})
                mensaje = self.recibir_mensaje(self.socket_cliente)
                if not mensaje:
                    raise ConnectionError
                respuesta = self.manejar_comando(mensaje)
                if not respuesta:
                    raise ConnectionError
            except ConnectionError:
                print("Ocurrió un error.")
                self.socket_cliente.close()
                break
            except OSError:
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

    def enviar(self, msg):
        mensaje_codificado = self.codificar_mensaje(msg)
        longitud_bytes_mensaje = len(mensaje_codificado).to_bytes(4, byteorder='big')
        enviar = longitud_bytes_mensaje + mensaje_codificado
        self.socket_cliente.sendall(enviar)

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
        return self.decodificar_mensaje(respuesta)
    
    def enviar2(self, msg):
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
        self.socket_cliente.sendall(enviar_msg)

    def recibir_input(self):
        # Inicia el thread que se encarga de manejar el input
        thread = threading.Thread(target=self.thread_recibir_input, daemon=True)
        thread.start()

    def manejar_comando(self, recibido):
        """
        Función que se llama al recibir un comando por parte del servidor.
        Se encarga de extraer los argumentos del mensaje y llamar a los
        métodos correspondientes.
        """
        datos = {}
        # Utilizamos if/elif/else para llamar al comando pertinente
        if 'credenciales' in recibido:
            self.senal_credenciales.emit(recibido['credenciales'])
            if all(recibido['credenciales'].values()):
                print('Usuario válido')
                if 'nombre' in recibido:
                    self.nombre = recibido['nombre']
            else:
                print('Usuario no creado')
        if 'jugadores' in recibido:
            datos['jugadores'] = recibido['jugadores']
        if 'retado' in recibido:
            datos['retado'] = recibido['retado']
            self.senal_actualizar_principal.emit(datos)
        if 'juego' in recibido:  # Abrir ventana juego si se acepto reto 
            answer = recibido['juego'][2]
            if answer:
                self.senal_reto_aceptado.emit(recibido)
            else:
                self.senal_reto_rechazado.emit(recibido)
        if 'apuesta_rival' in recibido:
            self.senal_apuesta_rival.emit(recibido['apuesta_rival'])
        if 'victoria' in recibido or 'derrota' in recibido:
            self.senal_juego_terminado.emit(recibido)
        if 'cheated' in recibido:
            self.senal_cheated.emit(recibido)
        if 'estado_jugadores' in recibido:
            datos['estado_jugadores'] = recibido['estado_jugadores']
        if 'desconectar' in recibido:
            self.salir() if recibido['desconectar'] else None
        self.senal_actualizar_principal.emit(datos)
        return recibido

    def thread_recibir_input(self):
        """
        Captura el input del usuario.

        Lee mensajes desde el terminal y después se pasan a `self.enviar()`.
        """
        self.evento_prints.wait()
        self.recibir_input()

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

    def desconectar_usuario(self):
        print("Conexión terminada.")
        diccionario = {'desconectar': self.nombre}
        if self.nombre:
            self.enviar(diccionario)
        else:
            self.socket_cliente.close()

    def salir(self):
        self.socket_cliente.close()
