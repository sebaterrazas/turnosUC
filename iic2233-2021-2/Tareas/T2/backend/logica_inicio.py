from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(tuple)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, nombre):
        credenciales_correctas = False
        if p.MIN_CARACTERES <= len(nombre) <= p.MAX_CARACTERES and nombre.isalnum():
            self.senal_abrir_juego.emit(nombre)
            credenciales_correctas = True
        self.senal_respuesta_validacion.emit((nombre, credenciales_correctas))

