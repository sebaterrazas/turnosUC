from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QListWidgetItem, QPushButton, QHBoxLayout
import os
import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


window_name, base_class = uic.loadUiType(os.path.join(*p["ruta_ventana_principal"]))


class VentanaPrincipal(window_name, base_class):
    senal_retar_jugador = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.nombre = 'CR7'
        self.esperando_respuesta = False
        self.rival = ''
        self.jugadores = {}
        self.botones = {}
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowIcon(QIcon(os.path.join(*p['ruta_logo_fondo _negro'])))

        # Imagen de la tarjeta
        pixeles = QPixmap(os.path.join(*p['ruta_tarjeta']))
        self.tarjeta.setPixmap(pixeles)
        self.tarjeta.setScaledContents(True)

        # Imagen del billete
        pixeles = QPixmap(os.path.join(*p['ruta_wones']))
        self.wones.setPixmap(pixeles)
        self.wones.setScaledContents(True)

        # Imagen del reloj
        pixeles = QPixmap(os.path.join(*p['ruta_reloj']))
        self.imagen_reloj.setPixmap(pixeles)
        self.imagen_reloj.setScaledContents(True)

    def agregar_estilo(self):
        for b in self.botones.values():
            b.show()
            b.setStyleSheet(p['stylesheet_boton'])

    def actualizar(self, datos):
        if 'jugadores' in datos:
            if datos['jugadores'] != self.jugadores:
                for b in self.botones.values():
                    b.hide()
                self.botones = {}
                self.jugadores = datos['jugadores']
                texto1 = ''
                for n, j in enumerate(datos['jugadores']):
                    texto1 += f'{n+1}.- {j}\n\n\n'
                    if j != self.nombre:
                        boton = QPushButton('Retar', self)
                        x, y = p['posicion_boton_inicial']
                        delta_y = p['separacion_vertical_botones']
                        w, h = p['tamano_boton']
                        boton.setGeometry(x, y + delta_y * n, w, h)
                        boton.clicked.connect(lambda state, name=j: self.retar_jugador(name))
                        self.botones[j] = boton
                self.lista_jugadores.setText(texto1)
                self.agregar_estilo()
        if 'estado_jugadores' in datos and self.nombre in datos['estado_jugadores']:
            if datos['estado_jugadores'][self.nombre]['estado'] == 'reto' \
                    and self.esperando_respuesta:
                for b in self.botones.values():
                    b.hide()
                    b.setEnabled(False)
                self.botones[self.rival].show()
                self.botones[self.rival].setText('Retado')
                self.botones[self.rival].setStyleSheet(p['stylesheet_boton_apretado'])
                self.texto_esperando.setText('Esperando respuesta...')
                self.texto_esperando.show()
                self.imagen_reloj.show()
            if datos['estado_jugadores'][self.nombre]['estado'] == 'sala_principal':
                for nom, est in datos['estado_jugadores'].items():
                    estado = est['estado']
                    if estado == 'reto' or estado == 'jugando':
                        try:
                            b = self.botones[nom]
                            b.setText('No habilitado')
                            b.setEnabled(False)
                            b.setStyleSheet(p['stylesheet_boton_desactivado'])
                        except KeyError:
                            pass
                    elif estado == 'sala_principal':
                        try:
                            b = self.botones[nom]
                            b.setText('Retar')
                            b.setEnabled(True)
                            b.setStyleSheet(p['stylesheet_boton'])
                        except KeyError:
                            pass

    def retar_jugador(self, rival):
        print(f'Retaste a {rival}')
        self.rival = rival
        self.esperando_respuesta = True
        self.senal_retar_jugador.emit((self.nombre, rival))

    def mostrar(self, n):
        self.texto_esperando.hide()
        self.imagen_reloj.hide()
        self.texto_esperando.hide()
        if type(n) == dict:
            n, rival, _ = n['juego']
            self.botones[rival].setEnabled(True)
            self.botones[rival].setText('Retar')
            self.botones[rival].setStyleSheet(p['stylesheet_boton'])
            if self.esperando_respuesta:
                self.texto_esperando.setText(f'{rival} rechazó tu\ninvitación')
                self.texto_esperando.show()
        self.nombre = n
        self.setWindowTitle(self.nombre)
        self.show()

    def ocultar(self):
        self.esperando_respuesta = False
        self.texto_esperando.hide()
        self.hide()
