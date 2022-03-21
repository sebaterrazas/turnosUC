from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
)
import json
import os

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):
        self.setWindowIcon(QIcon(os.path.join(*p['ruta_logo_fondo _negro'])))
        self.setGeometry(tamano_ventana)

        self.label1 = QLabel('Usuario: ', self)
        self.usuario_form = QLineEdit('', self)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.usuario_form)
        hbox1.addStretch(1)

        self.label2 = QLabel('Fecha de nacimiento: ', self)
        self.fecha_form = QLineEdit('DD/MM/YYYY', self)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.fecha_form)
        hbox2.addStretch(1)

        self.label3 = QLabel(self)
        self.label3.setMaximumSize(400, 400)

        # Cargamos la imagen como pixeles
        pixeles = QPixmap(os.path.join(*p['ruta_icono_blanco']))
        # Agregamos los pixeles al elemento QLabel
        self.label3.setPixmap(pixeles)
        self.label3.setScaledContents(True)
        hbox_imagen = QHBoxLayout()
        hbox_imagen.addStretch(1)
        hbox_imagen.addWidget(self.label3)
        hbox_imagen.addStretch(2)

        self.ingresar_button = QPushButton('Jugar', self)
        self.ingresar_button.setGeometry(20, 70, 360, 30)
        self.ingresar_button.clicked.connect(self.enviar_login)

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

        self.usuario_repetido = QMessageBox()
        label = QLabel()
        label.setText("Nombre de usuario ya existente, intenta con otro.")
        self.usuario_repetido.layout().addWidget(label)
        self.usuario_repetido.layout().setGeometry(QRect(80, 320, 300, 100))

        self.formato_no_valido = QMessageBox()
        label = QLabel()
        label.setText("Formato incorrecto.")
        self.formato_no_valido.layout().addWidget(label)
        self.formato_no_valido.layout().setGeometry(QRect(80, 320, 100, 200))

        self.servidor_lleno = QMessageBox()
        label = QLabel()
        label.setText("Servidor lleno :/")
        self.servidor_lleno.layout().addWidget(label)
        self.servidor_lleno.layout().setGeometry(QRect(80, 320, 100, 200))

        self.agregar_estilo()

    def enviar_login(self):
        usuario = self.usuario_form.text()
        fecha = self.fecha_form.text()
        self.senal_enviar_login.emit(usuario, fecha)

    def agregar_estilo(self):
        # Estilo extra
        self.setStyleSheet("background-color: rgb(10,10,10); color: white")
        self.usuario_form.setStyleSheet("background-color: white;"
                                        "border-radius: 5px;"
                                        "color: rgb(70,70,70)")
        self.fecha_form.setStyleSheet("background-color: white;"
                                        "border-radius: 5px;"
                                        "color: rgb(70,70,70)")
        self.ingresar_button.setStyleSheet(p['stylesheet_boton'])

    def recibir_validacion(self, tupla_respuesta):
        if all(tupla_respuesta.values()):
            self.ocultar()
        elif not tupla_respuesta['formato']:
            self.formato_no_valido.exec_()
        elif not tupla_respuesta['no_repetido']:
            self.usuario_repetido.exec_()
        elif not tupla_respuesta['servidor_disponible']:
            self.servidor_lleno.exec_()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.usuario_form.setText('')
        self.fecha_form.setText('DD/MM/YYYY')
        self.hide()
