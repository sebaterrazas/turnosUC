from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

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

        self.label2 = QLabel('Contraseña: ', self)
        self.clave_form = QLineEdit('', self)
        self.clave_form.setEchoMode(QLineEdit.Password)
        # self.label2.move(10, 23)
        # self.clave_form.setGeometry(75, 35, 100, 20)
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.clave_form)
        hbox2.addStretch(1)

        self.label3 = QLabel(self)
        self.label3.setMaximumSize(400, 400)

        # Cargamos la imagen como pixeles
        pixeles = QPixmap(p.RUTA_LOGO)
        # Agregamos los pixeles al elemento QLabel
        self.label3.setPixmap(pixeles)
        self.label3.setScaledContents(True)
        hbox_imagen = QHBoxLayout()
        hbox_imagen.addStretch(1)
        hbox_imagen.addWidget(self.label3)
        hbox_imagen.addStretch(2)

        self.ingresar_button = QPushButton('Ingresar', self)
        self.ingresar_button.setGeometry(20, 70, 360, 30)
        self.ingresar_button.clicked.connect(self.enviar_login)
        # self.ingresar_button.resize(self.ingresar_button.sizeHint())
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.ingresar_button)
        hbox3.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_imagen)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.agregar_estilo()

    def enviar_login(self):
        usuario = self.usuario_form.text()
        clave = self.clave_form.text()
        self.senal_enviar_login.emit((usuario, clave))

    def agregar_estilo(self):
        # Acciones y señales
        self.clave_form.returnPressed.connect(
            lambda: self.ingresar_button.click()
        )  # Permite usar "ENTER" para iniciar sesión

        # Estilo extra
        self.setStyleSheet("background-color: #fdf600")
        self.usuario_form.setStyleSheet("background-color: #000000;"
                                        "border-radius: 5px;"
                                        "color: white")
        self.clave_form.setStyleSheet("background-color: #000000;"
                                      "border-radius: 5px;"
                                      "color: white")
        self.ingresar_button.setStyleSheet(p.stylesheet_boton)

    def recibir_validacion(self, tupla_respuesta):
        if tupla_respuesta[1]:
            self.ocultar()
        else:
            self.clave_form.setText("")
            self.clave_form.setPlaceholderText("Contraseña inválida!")

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
