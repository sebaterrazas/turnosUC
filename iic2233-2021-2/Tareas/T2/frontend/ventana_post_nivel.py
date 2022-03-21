from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POST_NIVEL)


class VentanaPostNivel(window_name, base_class):
    senal_guardar_datos = pyqtSignal(dict)
    senal_sig_nivel = pyqtSignal(dict)
    senal_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.datos = {}
        self.setupUi(self)
        self.init_gui()

    def mostrar(self, dic):
        self.datos = dic
        nivel_superado = dic["nivel superado"]
        diccionario = {"Nombre": dic["sapo"].nombre,
                       "Nivel actual": dic["nivel"],
                       "Puntaje total": dic["puntaje total"],
                       "Puntaje nivel anterior": dic["puntaje ronda"],
                       "Vidas restantes": dic["sapo"].vidas,
                       "Total monedas": dic["sapo"].monedas
                       }
        text1 = ''
        text2 = ''
        for k, v in diccionario.items():
            text1 += f'\t\t{k}:\n\n\n'
            text2 += f'\t{v}\n\n\n'
        self.cuerpo.setText(text1)
        self.cuerpo_2.setText(text2)
        if nivel_superado:
            self.seguir_jugando.setText("           Puedes seguir jugando")
            self.seguir_jugando.setStyleSheet(p.stylesheet_nivel_superado)
            self.boton_tienda.hide()
        else:
            self.seguir_jugando.setText("    Perdiste, no puedes continuar :(")
            self.seguir_jugando.setStyleSheet(p.stylesheet_nivel_no_superado)
            self.boton_tienda.hide()
            self.boton_sig_nivel.hide()
            self.senal_guardar_datos.emit(self.datos)
        self.show()

    def init_gui(self):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.setWindowTitle("DCCrossy Frog -- Post Nivel")
        self.boton_salir.clicked.connect(self.salir)
        self.boton_sig_nivel.clicked.connect(self.sig_nivel)
        self.agregar_estilo()

    def agregar_estilo(self):
        # Estilo extra (además del que se puso en el Qt Designer)
        self.setStyleSheet("background-color: #fdf600")
        self.boton_salir.setStyleSheet(p.stylesheet_boton)
        self.boton_sig_nivel.setStyleSheet(p.stylesheet_boton)
        self.boton_tienda.setStyleSheet(p.stylesheet_boton)

    def sig_nivel(self):
        self.senal_sig_nivel.emit(self.datos)
        self.hide()

    def salir(self):
        self.hide()
        self.senal_inicio.emit()
