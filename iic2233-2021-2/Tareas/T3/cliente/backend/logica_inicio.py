from PyQt5.QtCore import QObject, pyqtSignal

import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(dict)
    senal_abrir_juego = pyqtSignal(str)
    senal_servidor_validacion = pyqtSignal(dict)
    senal_actualizar_ventana = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.nombre = ''

    def comprobar_usuario(self, nombre, fecha):
        self.nombre = nombre
        self.senal_servidor_validacion.emit({'validacion': {'nombre': nombre, 'fecha': fecha}})

    def validar_usuario(self, credenciales_correctas):
        if all(credenciales_correctas.values()):
            self.senal_abrir_juego.emit(self.nombre)
        self.senal_respuesta_validacion.emit(credenciales_correctas)
