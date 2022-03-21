from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
)


import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str)
    senal_ranking = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.setGeometry(tamano_ventana)

        self.label1 = QLabel('Usuario: ', self)
        self.usuario_form = QLineEdit('', self)
        # self.label1.move(10, 15)
        # self.usuario_form.setGeometry(75, 15, 100, 20)
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.usuario_form)
        hbox1.addStretch(1)

        self.label3 = QLabel(self)
        self.label3.setMaximumSize(400, 400)

        # Cargamos la imagen como pixeles
        pixeles = QPixmap(p.RUTA_ICONO)
        # Agregamos los pixeles al elemento QLabel
        self.label3.setPixmap(pixeles)
        self.label3.setScaledContents(True)
        hbox_imagen = QHBoxLayout()
        hbox_imagen.addStretch(1)
        hbox_imagen.addWidget(self.label3)
        hbox_imagen.addStretch(2)

        self.ingresar_button = QPushButton('Iniciar partida', self)
        self.ingresar_button.setGeometry(20, 70, 360, 30)
        self.ingresar_button.clicked.connect(self.enviar_login)

        self.ranking_button = QPushButton('Ver ranking', self)
        self.ranking_button.setGeometry(20, 70, 360, 30)
        self.ranking_button.clicked.connect(self.ranking)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.ingresar_button)
        hbox3.addStretch(1)
        hbox3.addWidget(self.ranking_button)
        hbox3.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_imagen)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.agregar_estilo()

        self.mensaje_derrota = QMessageBox()
        label = QLabel()
        label.setText("Usuario no válido")
        # label.setFont(QFont('Arial Font', 20))
        self.mensaje_derrota.layout().addWidget(label)
        self.mensaje_derrota.layout().setGeometry(QRect(80, 320, 300, 100))

    def enviar_login(self):
        usuario = self.usuario_form.text()
        self.senal_enviar_login.emit(usuario)

    def ranking(self):
        self.ocultar()
        self.senal_ranking.emit()

    def agregar_estilo(self):
        # Estilo extra
        self.setStyleSheet("background-color: #fdf600")
        self.usuario_form.setStyleSheet("background-color: rgb(11, 74, 8);"
                                        "border-radius: 5px;"
                                        "color: white")
        self.ingresar_button.setStyleSheet(p.stylesheet_boton)
        self.ranking_button.setStyleSheet(p.stylesheet_boton)

    def recibir_validacion(self, tupla_respuesta):
        if tupla_respuesta[1]:
            self.ocultar()
        else:
            self.mensaje_derrota.exec_()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
