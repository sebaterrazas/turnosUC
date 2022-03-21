from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
import os
import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


window_name, base_class = uic.loadUiType(os.path.join(*p["ruta_ventana_final"]))


class VentanaFinal(window_name, base_class):
    senal_volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.nombre = 'CR7'
        self.rival = 'Messi'
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowIcon(QIcon(os.path.join(*p['ruta_logo_fondo _negro'])))

        # Imagen tarjeta
        pixeles = QPixmap(os.path.join(*p['ruta_tarjeta']))
        self.imagen_tarjeta.setPixmap(pixeles)
        self.imagen_tarjeta.setScaledContents(True)
        self.nombre1.setStyleSheet(p['stylesheet_normal'])
        self.nombre2.setStyleSheet(p['stylesheet_normal'])

        # Botón inicio
        self.boton_inicio.clicked.connect(self.volver_inicio)

    def mostrar(self, dicc):
        if 'victoria' in dicc:
            self.resultado = 'victoria'

            self.nombre1.setStyleSheet(p['stylesheet_victoria'])

            pixeles = QPixmap(os.path.join(*p['ruta_wones']))
            self.imagen1.setPixmap(pixeles)
            self.imagen1.setScaledContents(True)

            pixeles = QPixmap(os.path.join(*p['ruta_calavera_gris']))
            self.imagen2.setPixmap(pixeles)
            self.imagen2.setScaledContents(True)
        else:
            self.resultado = 'derrota'

            self.nombre2.setStyleSheet(p['stylesheet_victoria'])

            pixeles = QPixmap(os.path.join(*p['ruta_wones']))
            self.imagen2.setPixmap(pixeles)
            self.imagen2.setScaledContents(True)

            pixeles = QPixmap(os.path.join(*p['ruta_calavera_gris']))
            self.imagen1.setPixmap(pixeles)
            self.imagen1.setScaledContents(True)

        self.razon = dicc[self.resultado]['razon']
        self.nombre = dicc[self.resultado]['nombre']
        self.rival = dicc[self.resultado]['rival']
        self.setWindowTitle(self.nombre)

        self.titulo.setText(f'{self.resultado.capitalize()} {self.razon}')
        self.nombre1.setText(f'{self.nombre}')
        self.nombre2.setText(f'{self.rival}')
        self.boton_inicio.setStyleSheet(p['stylesheet_boton'])
        self.show()

    def ocultar(self):
        self.hide()

    def volver_inicio(self):
        self.ocultar()
        self.senal_volver_inicio.emit()
