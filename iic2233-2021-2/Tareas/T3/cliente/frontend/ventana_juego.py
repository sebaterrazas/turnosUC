from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QMessageBox
import os
import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


window_name, base_class = uic.loadUiType(os.path.join(*p["ruta_ventana_juego"]))


class VentanaJuego(window_name, base_class):
    senal_apuesta_realizada = pyqtSignal(dict)
    senal_tecla = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.nombre = 'CR7'
        self.rival = 'Messi'
        self.paridad_oponente = ''
        self.apuesta_realizada = {}
        self.apuesta_rival = {}
        self.turno = False
        self.ganador = 'hbj'
        self.cant_apostada = -420
        self.cheatcode = ''
        self.canicas = p['canicas_iniciales']
        self.canicas_rival = p['canicas_iniciales']
        self.apuesta_mal_realizada = False
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowIcon(QIcon(os.path.join(*p['ruta_logo_fondo _negro'])))

        # Imagen del resultado
        pixeles = QPixmap(os.path.join(*p['ruta_reloj']))
        self.imagen_resultado.setPixmap(pixeles)
        self.imagen_resultado.setScaledContents(True)

        # Foto perfil 1
        pixeles = QPixmap(os.path.join(*p['ruta_foto1']))
        self.imagen_foto.setPixmap(pixeles)
        self.imagen_foto.setScaledContents(True)

        # Foto perfil 2
        pixeles = QPixmap(os.path.join(*p['ruta_foto2']))
        self.imagen_foto_2.setPixmap(pixeles)
        self.imagen_foto_2.setScaledContents(True)

        # Botón aceptar
        self.boton_aceptar.clicked.connect(self.realizar_apuesta)

    def keyPressEvent(self, event):
        if event.text().upper() == 'F':
            self.senal_tecla.emit('F')
        if event.text().upper() == 'A':
            self.senal_tecla.emit('A')
        if event.text().upper() == 'Z':
            self.senal_tecla.emit('Z')
        if event.text().upper() == 'X':
            self.senal_tecla.emit('X')

    def realizar_apuesta(self):
        if self.turno:
            if self.boton_par.isChecked():
                self.paridad_oponente = 'par'
                self.apuesta_mal_realizada = False
            elif self.boton_impar.isChecked():
                self.paridad_oponente = 'impar'
                self.apuesta_mal_realizada = False
            else:
                self.apuesta_mal_realizada = True
            if not self.apuesta_mal_realizada:
                self.boton_aceptar.setText('Apostado')
                self.boton_aceptar.setEnabled(False)
                self.boton_aceptar.setStyleSheet(p['stylesheet_boton_apretado'])
                self.senal_apuesta_realizada.emit({
                    'rival': self.rival,
                    'cantidad_apostada': self.spin_apuesta.value(),
                    'paridad_oponente': self.paridad_oponente,
                    'nombre': self.nombre
                })
        else:
            self.boton_aceptar.setText('Apostado')
            self.boton_aceptar.setEnabled(False)
            self.boton_aceptar.setStyleSheet(p['stylesheet_boton_apretado'])
            self.senal_apuesta_realizada.emit({
                'rival': self.rival,
                'cantidad_apostada': self.spin_apuesta.value(),
                'nombre': self.nombre
            })

    def actualizar(self, dicc):
        self.spin_apuesta.clearFocus()
        if 'canicas' in dicc:
            self.canicas = dicc['canicas']
            self.texto_canicas.setText(f'Cantidad canicas: {self.canicas}')
        if 'canicas_rival' in dicc:
            self.canicas_rival = dicc['canicas_rival']
            self.texto_canicas_2.setText(f'Cantidad canicas: {self.canicas_rival}')
        self.spin_apuesta.setMaximum(self.canicas)
        if 'apuesta_hecha' in dicc:
            self.apuesta_realizada = dicc['apuesta_hecha']
        if 'apuesta_rival' in dicc:
            self.apuesta_rival = dicc['apuesta_rival']
        if 'cheat' in dicc:
            self.cheatcode = dicc['cheat']
        if not self.apuesta_realizada:
            tiempo_restante = dicc['tiempo_restante']
            self.resultado.setText(f'Tiempo restante:\n{tiempo_restante} s')
        else:
            self.resultado.setText(f'Esperando a\n{self.rival}')
        if self.apuesta_rival:
            self.texto_apuesta_rival.setText('Rival listo')
            self.texto_apuesta_rival_2.setText('Rival listo')
        if self.cheatcode:
            # Pop-up cheatcode
            self.cheatcode_msg = QMessageBox()
            label = QLabel()
            label.setText(f"Psss... Tu rival va a apostar una cantidad {self.cheatcode} de canicas")
            self.cheatcode_msg.layout().addWidget(label)
            self.cheatcode_msg.layout().setGeometry(QRect(80, 320, 100, 200))
            self.cheatcode_msg.exec()
        if 'turno' in dicc:
            self.turno = dicc['turno']
        if self.turno:
            self.texto_paridad.show()
            self.boton_par.setAutoExclusive(True)
            self.boton_impar.setAutoExclusive(True)
            self.boton_par.show()
            self.boton_impar.show()
        else:
            self.texto_paridad.hide()
            self.boton_par.hide()
            self.boton_par.setAutoExclusive(False)
            self.boton_par.setChecked(False)
            self.boton_impar.hide()
            self.boton_impar.setAutoExclusive(False)
            self.boton_impar.setChecked(False)
        if 'ganador' in dicc:
            self.ganador = dicc['ganador']
        if 'cant_apuesta' in dicc:
            self.cant_apostada = dicc['cant_apuesta']
        if self.ganador == self.nombre:
            self.boton_aceptar.hide()
            self.resultado.setText(f'{self.nombre} ganó\n{self.cant_apostada}')
            self.resultado.show()
            pixeles = QPixmap(os.path.join(*p['ruta_calavera_rosada']))
            self.imagen_resultado.setPixmap(pixeles)
            self.imagen_resultado.setScaledContents(True)
            self.imagen_resultado.show()
        elif self.ganador == self.rival:
            self.boton_aceptar.hide()
            self.resultado.setText(f'{self.rival} ganó\n{self.cant_apostada}')
            self.resultado.show()
            pixeles = QPixmap(os.path.join(*p['ruta_calavera_rosada']))
            self.imagen_resultado.setPixmap(pixeles)
            self.imagen_resultado.setScaledContents(True)
            self.imagen_resultado.show()
        if 'new_round' in dicc:
            if dicc['new_round']:
                self.boton_aceptar.setText('Apostar')
                self.boton_aceptar.setEnabled(True)
                self.boton_aceptar.setStyleSheet(p['stylesheet_boton'])
                self.boton_aceptar.show()
                self.texto_apuesta_rival.setText('Esperando...')
                self.texto_apuesta_rival_2.setText('Esperando...')

    def mostrar(self, dicc):
        self.nombre = dicc['juego'][0]
        self.rival = dicc['juego'][1]
        self.setWindowTitle(self.nombre)
        self.boton_aceptar.setText('Apostar')
        self.spin_apuesta.setValue(1)
        self.spin_apuesta.setMinimum(1)
        self.spin_apuesta.clearFocus()
        self.boton_par.setChecked(False)
        self.boton_impar.setChecked(False)
        self.canicas = p['canicas_iniciales']
        self.canicas_rival = p['canicas_iniciales']
        self.texto_canicas.setText(f'Cantidad canicas: {self.canicas_rival}')
        self.texto_canicas_2.setText(f'Cantidad canicas: {self.canicas_rival}')
        self.nombre_1.setText(f'Personaje: {self.nombre}')
        self.nombre_2.setText(f'Rival: {self.rival}')
        self.resultado.setText(f'Tiempo restante:\n{p["tiempo_turno"]} s')
        self.texto_paridad.hide()
        self.boton_par.hide()
        self.boton_impar.hide()
        self.show()

    def ocultar(self):
        self.hide()
