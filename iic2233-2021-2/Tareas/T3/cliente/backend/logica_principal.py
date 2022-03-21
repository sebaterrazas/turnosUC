from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect
import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


class LogicaPrincipal(QObject):

    senal_actualizar_ventana = pyqtSignal(dict)
    senal_retar_rival = pyqtSignal(dict)
    senal_retado = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.nombre = ''
        self.jugadores = {}

    def actualizar(self, datos):
        self.jugadores = datos['jugadores'] if 'jugadores' in datos else {}
        self.senal_actualizar_ventana.emit(datos)
        if 'retado' in datos:
            self.senal_retado.emit(datos)

    def retar_rival(self, tupla):
        diccionario = {'retar': {'retador': tupla[0], 'retado': tupla[1]}}
        self.senal_retar_rival.emit(diccionario)


class Player(QObject):
    def __init__(self):
        super().__init__()
        self.nombre = ''

    def definir_nombre(self, n):
        self.nombre = n
