from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel
import parametros as p
import random

#todo PONER EN README QUE ME BASÉ EN AS3!!!

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):
    senal_iniciar_juego = pyqtSignal()
    senal_pausa = pyqtSignal()
    senal_tecla = pyqtSignal(str)
    senal_continuar = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.autos = {}
        self.troncos = {}
        self.items = {}
        self.mapa = ''
        self.pausado = False
        self.direccion_sapo = 'Q'
        self.pos_numero = [1, 2, 3, 2]
        self.setupUi(self)
        self.init_gui()

    def mostrar_ventana(self):
        self.show()
        self.senal_iniciar_juego.emit()
        self.casilla_vidas.setText('* * *')
        self.casilla_puntaje.setText('0 puntos')
        self.casilla_nivel.setText('1')
        self.casilla_monedas.setText('$ 0')
        self.casilla_tiempo.setText('- s')

    def sig_nivel(self, dic):
        for k, a in self.autos.items():
            a.hide()
        for k, t in self.troncos.items():
            t.hide()
        for k, i in self.items.items():
            i.hide()
        self.autos = {}
        self.troncos = {}
        self.items = {}
        self.mapa = ''
        self.pausado = False
        self.direccion_sapo = 'Q'
        self.pos_numero = [1, 2, 3, 2]
        self.show()
        self.senal_iniciar_juego.emit()
        self.casilla_vidas.setText('* ' * dic['sapo'].vidas)
        self.casilla_puntaje.setText(f'{dic["puntaje total"]} puntos')
        self.casilla_nivel.setText(str(dic["nivel"] + 1))
        self.casilla_monedas.setText('$ ' + str(dic['sapo'].monedas))
        self.casilla_tiempo.setText('- s')

    def keyPressEvent(self, event):
        if event.text() == p.TECLA_PAUSA:
            self.senal_tecla.emit('P')
            self.pausa()

        if not self.pausado:
            if event.text() == p.TECLA_SALTO:
                self.senal_tecla.emit('J')
            if event.text() == p.TECLA_ARRIBA:
                self.senal_tecla.emit('U')
            if event.text() == p.TECLA_IZQUIERDA:
                self.senal_tecla.emit('L')
            if event.text() == p.TECLA_DERECHA:
                self.senal_tecla.emit('R')
            if event.text() == p.TECLA_ABAJO:
                self.senal_tecla.emit('D')

            if event.text() == p.TECLA_D:
                self.senal_tecla.emit('d')
            if event.text() == p.TECLA_I:
                self.senal_tecla.emit('i')
            if event.text() == p.TECLA_V:
                self.senal_tecla.emit('v')
            if event.text() == p.TECLA_N:
                self.senal_tecla.emit('n')

    def init_gui(self):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.setWindowTitle("DCCrossy Frog")

        self.icono = QPixmap(p.RUTA_ICONO)
        self.imagen_pasto = QPixmap(p.RUTA_PASTO)
        self.imagen_icono.setPixmap(self.icono)
        self.imagen_icono.setScaledContents(True)
        self.fondo_juego.setPixmap(self.imagen_pasto)
        self.fondo_juego.setScaledContents(True)

        self.boton_salir.clicked.connect(self.salir)
        self.boton_pausa.clicked.connect(self.pausa)
        self.iniciar_sapo()

    def iniciar_sapo(self):
        self.sapo = QLabel("", self)
        self.pixeles_sapo = QPixmap(p.RUTA_SAPO_VERDE_QUIETO)
        self.sapo.setPixmap(self.pixeles_sapo)
        self.sapo.setScaledContents(True)
        self.sapo.resize(p.WIDTH_SAPO, p.HEIGHT_SAPO)
        self.sapo.move(p.X_INICIAL, p.Y_INICIAL)
        self.sapo.setFocus()

    def generar_mapa(self, mapa):
        for i, m in enumerate(mapa):
            m = m[0]
            if m == 'C':
                self.imagen = QPixmap(p.RUTA_CARRETERA)
            elif m == 'R':
                self.imagen = QPixmap(p.RUTA_RIO)
            if i == 0:
                fondo = self.toplane
            elif i == 1:
                fondo = self.midlane
            else:
                fondo = self.botlane
            fondo.setPixmap(self.imagen)
            fondo.setScaledContents(True)

    def generar_auto(self, a):
        self.auto = QLabel("", self)
        ruta_auto = random.choice(p.RUTAS_AUTOS_DER)
        if a.direccion == 'L':
            ruta_auto = random.choice(p.RUTAS_AUTOS_IZQ)
        self.pixeles_auto = QPixmap(ruta_auto)
        self.auto.setPixmap(self.pixeles_auto)
        self.auto.setScaledContents(True)
        self.auto.resize(p.WIDTH_AUTO, p.HEIGHT_AUTO)
        y_inicial = a.cuerpo.y()
        x_inicial = a.cuerpo.x()
        self.auto.move(x_inicial, y_inicial)
        self.auto.show()
        self.autos[a.numero] = self.auto  # Añado key al diccionario

    def generar_tronco(self, t):
        self.tronco = QLabel("", self)
        self.pixeles_tronco = QPixmap(p.RUTA_TRONCO)
        self.tronco.setPixmap(self.pixeles_tronco)
        self.tronco.setScaledContents(True)
        self.tronco.resize(p.WIDTH_TRONCO, p.HEIGHT_TRONCO)
        y_inicial = t.cuerpo.y()
        x_inicial = t.cuerpo.x()
        self.tronco.move(x_inicial, y_inicial)
        self.tronco.show()
        self.troncos[t.numero] = self.tronco

    def generar_item(self, i):
        self.item = QLabel("", self)
        ruta = p.RUTA_TIPOS[i.tipo]
        self.pixeles_item = QPixmap(ruta)
        self.item.setPixmap(self.pixeles_item)
        self.item.setScaledContents(True)
        self.item.resize(p.WIDTH_ITEM, p.HEIGHT_ITEM)
        y_inicial = i.cuerpo.y()
        x_inicial = i.cuerpo.x()
        self.item.move(x_inicial, y_inicial)
        self.item.show()
        self.item.raise_()
        self.items[i.numero] = self.item

    def consumir_item(self, i):
        if i in self.items:
            self.items[i].hide()

    def cambiar_puntaje(self, puntaje):
        self.casilla_puntaje.setText(str(puntaje))

    def fin_del_juego(self):
        self.mensaje_derrota.exec_()

    def salir(self):
        self.close()

    def pausa(self):
        if self.boton_pausa.text() == 'Pausa':
            self.boton_pausa.setText('Continuar')
            self.senal_pausa.emit()
        else:
            self.boton_pausa.setText('Pausa')
            self.senal_continuar.emit()
        self.pausado = not self.pausado

    def movimiento(self):
        numero = self.pos_numero.pop(0)
        self.pos_numero.append(numero)
        if self.direccion_sapo == 'U':
            if numero == 1:
                ruta = p.RUTA_SAPO_VERDE_ARRIBA1
            elif numero == 2:
                ruta = p.RUTA_SAPO_VERDE_ARRIBA2
            elif numero == 3:
                ruta = p.RUTA_SAPO_VERDE_ARRIBA3

        elif self.direccion_sapo == 'D':
            if numero == 1:
                ruta = p.RUTA_SAPO_VERDE_ABAJO1
            elif numero == 2:
                ruta = p.RUTA_SAPO_VERDE_ABAJO2
            elif numero == 3:
                ruta = p.RUTA_SAPO_VERDE_ABAJO3

        elif self.direccion_sapo == 'R':
            if numero == 1:
                ruta = p.RUTA_SAPO_VERDE_DERECHA1
            elif numero == 2:
                ruta = p.RUTA_SAPO_VERDE_DERECHA2
            elif numero == 3:
                ruta = p.RUTA_SAPO_VERDE_DERECHA3

        elif self.direccion_sapo == 'L':
            if numero == 1:
                ruta = p.RUTA_SAPO_VERDE_IZQUIERDA1
            elif numero == 2:
                ruta = p.RUTA_SAPO_VERDE_IZQUIERDA2
            elif numero == 3:
                ruta = p.RUTA_SAPO_VERDE_IZQUIERDA3

        else:
            ruta = p.RUTA_SAPO_VERDE_QUIETO

        self.pixeles_sapo = QPixmap(ruta)
        self.sapo.setPixmap(self.pixeles_sapo)
        self.sapo.setScaledContents(True)

    def actualizar(self, dic):
        if dic['nivel superado']:
            self.hide()
        frog = dic['sapo'].cuerpo
        self.sapo.move(frog.x(), frog.y())

        self.direccion_sapo = dic['sapo'].direccion
        self.movimiento()

        tiempo = dic['tiempo']
        self.casilla_tiempo.setText(str(int(tiempo)) + ' s')
        puntaje = dic['puntaje']
        self.casilla_puntaje.setText(str(int(puntaje)))

        mapa = dic['mapa']
        if not self.mapa:
            self.generar_mapa(mapa)

        for a in dic['autos']:
            if a.numero not in self.autos:  # self.autos un diccionario
                self.generar_auto(a)
        for a in dic['autos']:
            self.autos[a.numero].move(a.cuerpo.x(), a.cuerpo.y())  # Actualizo los autos

        for t in dic['troncos']:
            if t.numero not in self.troncos:
                self.generar_tronco(t)

        for t in dic['troncos']:
            self.troncos[t.numero].move(t.cuerpo.x(), t.cuerpo.y())

        for i in dic['items']:
            if i.numero not in self.items:
                self.generar_item(i)
        for k, i in self.items.items():
            i.raise_()

        vidas = dic['sapo'].vidas
        self.casilla_vidas.setText(vidas * '*')
        monedas = dic['sapo'].monedas
        self.casilla_monedas.setText('$' + str(monedas))
        self.sapo.raise_()


