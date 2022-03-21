from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect
import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


class LogicaReto(QObject):
    senal_reto_aceptado = pyqtSignal(dict)
    senal_reto_rechazado = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def respuesta_reto(self, tupla):
        resp = {}
        resp['respuesta_reto'] = {'retador': tupla[0], 'retado': tupla[1], 'respuesta': tupla[2]}
        if tupla[2]:
            self.senal_reto_aceptado.emit(resp)
        else:
            self.senal_reto_rechazado.emit(resp)
