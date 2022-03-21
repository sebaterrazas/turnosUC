from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
import parametros as p
import os

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_RANKING)


class VentanaRanking(window_name, base_class):
    senal_regresar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def mostrar_ventana(self):
        self.show()

    def init_gui(self):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.setWindowTitle("DCCrossy Frog -- Ranking")
        self.boton_regresar.clicked.connect(self.regresar)
        self.ranking()
        self.agregar_estilo()

    def agregar_estilo(self):
        # Estilo extra (además del que se puso en el Qt Designer)
        self.setStyleSheet("background-color: #fdf600")
        self.boton_regresar.setStyleSheet(p.stylesheet_boton)

    def ranking(self):
        if os.path.isfile('puntajes.txt'):
            with open('puntajes.txt', 'r', encoding='utf-8') as file:
                ranking = [(r.split(',')[0], int(r.rstrip().split(',')[1])) for r in file.readlines()]
            ranking.sort(key=lambda x: x[1], reverse=True)
            text1 = ''
            text2 = ''
            for i, r in enumerate(ranking):
                if i < 5:
                    text1 += f'\t\t{i+1}.-   {r[0]}\n\n\n'
                    text2 += f'{r[1]} puntos\n\n\n'
        else:
            text1 = 'NO HAY REGISTRO DE\n\nNINGUNA PARTIDA'
            text2 = ''
        self.cuerpo.setText(text1)
        self.cuerpo_2.setText(text2)

    def regresar(self):
        self.hide()
        self.senal_regresar.emit()
