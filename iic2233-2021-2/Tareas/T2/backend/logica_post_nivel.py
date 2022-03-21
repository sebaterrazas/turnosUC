from PyQt5.QtCore import QObject


class LogicaPostNivel(QObject):

    def __init__(self):
        super().__init__()

    def guardar_datos(self, dic):
        with open('puntajes.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n{dic["sapo"].nombre},{dic["puntaje total"]}')


