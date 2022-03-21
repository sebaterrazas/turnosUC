from PyQt5.QtCore import QObject, pyqtSignal, QTimer
import json

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)


class LogicaJuego(QObject):
    senal_respuesta_reto = pyqtSignal(dict)
    senal_actualizar = pyqtSignal(dict)
    senal_apuesta_hecha = pyqtSignal(dict)
    senal_fin_juego = pyqtSignal(dict)
    senal_cheatcode = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.__canicas = p['canicas_iniciales']
        self.__canicas_rival = p['canicas_iniciales']
        self.tiempo_turno = p['tiempo_turno']
        self.teclas_apretadas = []
        self.parar_tiempo = False
        self.cheat = ''
        self.turno = True
        self.new_round = False
        self.ganador = 'CR7'
        self.perdedor = 'Messi'
        self.cantidad_apostada = -1
        self.apuesta_rival = {}
        self.apuesta_realizada = {}
        self.instanciar_timer()

    @property
    def tiempo(self):
        return self.__tiempo

    @tiempo.setter
    def tiempo(self, t):
        if t < self.tiempo_turno:
            self.__tiempo = round(t, 5)
        else:
            self.__tiempo = self.tiempo_turno - 1
            self.ronda_terminada(afk=True)

    @property
    def canicas(self):
        return self.__canicas

    @canicas.setter
    def canicas(self, c):
        if c > 0:
            self.__canicas = int(c)
        else:
            self.__canicas = 0
            self.derrota()

    @property
    def canicas_rival(self):
        return self.__canicas_rival

    @canicas_rival.setter
    def canicas_rival(self, cr):
        if cr > 0:
            self.__canicas_rival = int(cr)
        else:
            self.__canicas_rival = 0
            self.victoria()

    def instanciar_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timer_tick)

    def iniciar_juego(self, dicc):
        self.nombre = dicc['juego'][0]
        self.rival = dicc['juego'][1]
        self.turno = dicc['juego'][3]
        self.canicas = p['canicas_iniciales']
        self.canicas_rival = p['canicas_iniciales']
        self.timer.start()
        self.tiempo = 0
        self.i = 0

    def manejo_tecla(self, t):
        self.teclas_apretadas.append(t)

    def timer_tick(self):
        self.tiempo += 0.5 if not self.parar_tiempo else 0
        self.new_round = False
        if self.parar_tiempo:
            self.i += 0.5
            if self.i == 5:
                self.apuesta_rival = {}
                self.apuesta_realizada = {}
                self.i = 0
                self.parar_tiempo = False
                self.new_round = True
                self.turno = not self.turno
                self.ganador = 'CR7'
                self.perdedor = 'Messi'
        if self.apuesta_rival and self.apuesta_realizada:
            self.ronda_terminada(afk=False)
        if 'F' in self.teclas_apretadas and 'A' in self.teclas_apretadas:  # cheatcode 1
            if 'paridad_oponente' in self.apuesta_rival:
                self.cheat = str(self.apuesta_rival['paridad_oponente'])
            elif 'cantidad_apostada' in self.apuesta_rival:
                self.cheat = str(self.apuesta_rival['cantidad_apostada'])
        if 'Z' in self.teclas_apretadas and 'X' in self.teclas_apretadas:  # cheatcode 2
            canicas_robadas = min(self.canicas_rival, 3)
            self.canicas += canicas_robadas
            self.canicas_rival -= canicas_robadas
            self.senal_cheatcode.emit({'cheatcode':
                                                   {'nombre': self.nombre,
                                                    'rival': self.rival,
                                                    'canicas_robadas': canicas_robadas}})
        self.teclas_apretadas = []
        self.senal_actualizar.emit({
            'tiempo_restante': int(self.tiempo_turno-self.tiempo),
            'apuesta_hecha': bool(self.apuesta_realizada),
            "apuesta_rival": self.apuesta_rival,
            'apuesta_realizada': self.apuesta_realizada,
            'cheat': self.cheat,
            'canicas': self.canicas,
            'canicas_rival': self.canicas_rival,
            'turno': self.turno,
            'ganador': self.ganador,
            'perdedor': self.perdedor,
            'cant_apuesta': self.cantidad_apostada,
            'new_round': self.new_round
        })
        self.cheat = ''

    def apuesta_hecha(self, dicc):
        self.ronda_terminada(afk=False)
        self.apuesta_realizada = dicc
        self.senal_apuesta_hecha.emit({
            'apuesta_realizada': dicc
        })

    def rival_ha_apostado(self, dicc):
        self.apuesta_rival = dicc

    def ronda_terminada(self, afk):
        if self.apuesta_rival and self.apuesta_realizada:
            self.parar_tiempo = True
            self.tiempo = 0
            if 'paridad_oponente' in self.apuesta_realizada:
                if self.apuesta_rival['cantidad_apostada'] % 2:
                    par_rival = 'impar'
                else:
                    par_rival = 'par'
                if self.apuesta_realizada['paridad_oponente'] == par_rival:
                    self.ganador = self.nombre
                    self.perdedor = self.rival
                else:
                    self.perdedor = self.nombre
                    self.ganador = self.rival
                self.cantidad_apostada = self.apuesta_realizada['cantidad_apostada']
            elif 'paridad_oponente' in self.apuesta_rival:
                if self.apuesta_realizada['cantidad_apostada'] % 2:
                    par_rival = 'impar'
                else:
                    par_rival = 'par'
                if self.apuesta_rival['paridad_oponente'] != par_rival:
                    self.ganador = self.nombre
                    self.perdedor = self.rival
                else:
                    self.perdedor = self.nombre
                    self.ganador = self.rival
                self.cantidad_apostada = self.apuesta_rival['cantidad_apostada']
            if self.ganador == self.nombre:
                self.canicas += self.cantidad_apostada
                self.canicas_rival -= self.cantidad_apostada
            else:
                self.canicas -= self.cantidad_apostada
                self.canicas_rival += self.cantidad_apostada
            self.apuesta_rival = {}
            self.apuesta_realizada = {}
        if afk:
            print('¡Perdiste por AFK!')
            self.senal_fin_juego.emit({
                'derrota': {
                    'nombre': self.nombre,
                    'rival': self.rival,
                    'razon': 'por AFK'
                }
            })

    def derrota(self):
        self.detener_tiempo()
        self.senal_fin_juego.emit({
            'derrota': {
                'nombre': self.nombre,
                'rival': self.rival,
                'razon': ''
            }
        })

    def victoria(self):
        self.detener_tiempo()
        self.senal_fin_juego.emit({
            'victoria': {
                'nombre': self.nombre,
                'rival': self.rival,
                'razon': ''
            }
        })

    def cheated(self, dicc):
        canicas_robadas = dicc['cheatcode']['canicas_robadas']
        self.canicas -= canicas_robadas
        self.canicas_rival += canicas_robadas

    def detener_tiempo(self):
        self.timer.stop()

