import json
import socket
import threading
from os.path import join

import parametros as p
from manejo_archivos import (
    leer_unidad, guardar_archivo, almacenamiento_utilizado, iniciar_sistema,
)


class Servidor:
    _id_cliente = 1

    def __init__(self, host, port):
        print("Inicializando servidor...")

        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Clientes actualmente conectados al servidor
        self.clientes_conectados = {}
        iniciar_sistema()
        self.lock_archivos = threading.Lock()

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
                print("Conexión aceptada desde", address)
                socket_cliente.sendall("Gracias por conectarte\n".encode("utf-8"))
                self.clientes_conectados[Servidor._id_cliente] = socket_cliente
                thread_cliente = threading.Thread(target=self.thread_escuchar_cliente,
                                                  kwargs={"socket_cliente": socket_cliente,
                                                          "id_cliente": Servidor._id_cliente})
                Servidor._id_cliente += 1
                thread_cliente.start()
                socket_cliente.sendall("Gracias por conectarte\n".encode("utf-8"))
                # socket_cliente.close()
            except ConnectionError:
                print("Ocurrió un error.")
                break

    def thread_escuchar_cliente(self, socket_cliente, id_cliente):
        while True:
            try:
                mensaje = self.recibir_mensaje(socket_cliente)
                if not mensaje:
                    raise ConnectionError
                diccionario = {"comando": mensaje}
                respuesta = self.manejar_comando(diccionario, socket_cliente)
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
        sock_cliente.send(longitud_bytes_mensaje + mensaje_codificado)

    def manejar_comando(self, recibido, socket_cliente):
        comando = recibido["comando"]
        print("Comando recibido:", comando)
        respuesta = {}

        if comando == "explorar":
            respuesta["comando"] = "explorar"
            respuesta["argumentos"] = {"contenido": leer_unidad()}

        elif comando == "explorar_descargar":
            respuesta["comando"] = "explorar_descargar"
            respuesta["argumentos"] = {"contenido": leer_unidad()}

        elif comando == "almacenamiento":
            data_unidad = leer_unidad()
            uso = almacenamiento_utilizado(data_unidad)
            respuesta["comando"] = "almacenamiento"
            respuesta["argumentos"] = {"contenido": uso}

        elif comando == "subir":
            bytes_archivo = recibido["argumentos"]["contenido"]
            archivo = bytes.fromhex(bytes_archivo)
            tipo = recibido["argumentos"]["tipo"]
            nombre = recibido["argumentos"]["nombre"]
            with self.lock_archivos:
                exito = guardar_archivo(archivo, tipo, nombre)
            if exito:
                respuesta["comando"] = "exito"
            else:
                respuesta["comando"] = "error"
                respuesta["argumentos"] = {"mensaje": "El archivo ya existe"}

        elif comando == "descargar":
            tipo = recibido["argumentos"]["tipo"]
            nombre = recibido["argumentos"]["nombre"]
            ruta = join(p.RUTA_DATOS[tipo], nombre)
            msg = {
                "comando": "archivo",
                "argumentos": {
                    "ruta": ruta
                }
            }
            self.enviar(msg, socket_cliente)
            self.enviar_archivo(socket_cliente, ruta)
        return respuesta

    def enviar_archivo(self, socket_cliente, ruta):
        """
        Recibe una ruta a un archivo a enviar y los separa en chunks de 8 kb
        """
        with open(ruta, 'rb') as archivo:
            chunk = archivo.read(8000)
            largo = len(chunk)
            while largo > 0:
                chunk = chunk.ljust(8000, b'\0')    # Padding
                msg = {
                    "comando": "chunk",
                    "argumentos": {
                        "largo": largo,
                        "contenido": chunk.hex()
                    }
                }
                self.enviar(msg, socket_cliente)
                chunk = archivo.read(8000)
                largo = len(chunk)

    @staticmethod
    def codificar_mensaje(mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            return mensaje_bytes
        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje.')

    @staticmethod
    def decodificar_mensaje(msg_bytes):
        try:
            mensaje = json.loads(msg_bytes)
            return mensaje
        except json.JSONDecodeError:
            print('No se pudo decodificar el mensaje.')
            return dict()
