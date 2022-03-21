from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QListWidgetItem, QPushButton, QHBoxLayout
import os
import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


window_name, base_class = uic.loadUiType(os.path.join(*p["ruta_ventana_reto"]))


class VentanaReto(window_name, base_class):
    senal_retar_jugador = pyqtSignal(tuple)
    senal_respuesta_reto = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.nombre = 'CR7'
        self.rival = 'Messi'
        self.setupUi(self)
        self.botones = []
        self.init_gui()

    def init_gui(self):
        self.setWindowIcon(QIcon(os.path.join(*p['ruta_logo_fondo _negro'])))

        # Imagen de la tarjeta
        pixeles = QPixmap(os.path.join(*p['ruta_tarjeta']))
        self.imagen_tarjeta.setPixmap(pixeles)
        self.imagen_tarjeta.setScaledContents(True)

        # Imagen del billete
        pixeles = QPixmap(os.path.join(*p['ruta_icono_blanco']))
        self.imagen_logo.setPixmap(pixeles)
        self.imagen_logo.setScaledContents(True)

        self.boton_aceptar.clicked.connect(self.aceptar_reto)
        self.boton_rechazar.clicked.connect(self.rechazar_reto)

        self.botones.extend([self.boton_aceptar, self.boton_rechazar])

        self.agregar_estilo()

    def agregar_estilo(self):
        for b in self.botones:
            b.show()
            b.setStyleSheet(p['stylesheet_boton'])

    def aceptar_reto(self):
        print('Reto aceptado')
        self.ocultar()
        self.senal_respuesta_reto.emit((self.rival, self.nombre, True))

    def rechazar_reto(self):
        print('Reto rechazado')
        self.ocultar()
        self.senal_respuesta_reto.emit((self.rival, self.nombre, False))

    def mostrar(self, dicc):
        self.nombre = dicc['retado']['retado']
        self.rival = dicc['retado']['retador']
        self.setWindowTitle(self.nombre)
        self.titulo.setText(f'¡{self.rival} te ha invitado a jugar!')
        self.show()

    def ocultar(self):
        self.hide()
