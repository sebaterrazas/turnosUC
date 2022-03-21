import random

from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect

import parametros as p


class LogicaJuego(QObject):

    senal_actualizar = pyqtSignal(dict)
    senal_item_agarrado = pyqtSignal(str)
    senal_avanzar_nivel = pyqtSignal(dict)

    def __init__(self, sapo):
        super().__init__()
        self.nivel = 1
        self.puntaje = 0
        self.sapo = sapo
        self.mapas = p.MAPAS
        self.posibles_direcciones = p.DIRECCIONES
        self.__tiempo = 0  # En segundos
        self.tiempo_max = p.DURACION_RONDA_INICIAL
        self.velocidad_troncos = p.VELOCIDAD_TRONCOS
        self.velocidad_autos = p.VELOCIDAD_AUTOS
        self.iniciar_nivel()

    def iniciar_nivel(self):
        self.mapa = []
        self.autos = []
        self.troncos = []
        self.items = []
        self.instanciar_timer()
        self.avanzar = []
        self.cheatcode = []
        self.post_nivel = False
        self.check_point = False

    @property
    def tiempo(self):
        return self.__tiempo

    @tiempo.setter
    def tiempo(self, t):
        if t < self.tiempo_max:
            self.__tiempo = round(t, 5)
        else:
            self.__tiempo = self.tiempo_max
            self.nivel_superado(superado=False)
            self.detener_juego()

    def instanciar_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000/p.FPS)
        self.timer.timeout.connect(self.timer_tick)

    def iniciar_juego(self):
        self.timer.start()
        self.tiempo = 0
        self.pausa = False

    def sig_nivel(self, dic):
        self.sapo.cuerpo.moveTo(p.X_INICIAL, p.Y_INICIAL)
        self.puntaje = dic["puntaje total"]
        self.sapo.monedas = dic["sapo"].monedas
        self.sapo.vidas = dic['sapo'].vidas
        self.nivel += 1
        self.tiempo_max *= p.PONDERADOR_DIFICULTAD
        self.velocidad_troncos = p.VELOCIDAD_TRONCOS * \
                                 (2 / (1 + p.PONDERADOR_DIFICULTAD)) ** self.nivel
        self.velocidad_autos = p.VELOCIDAD_AUTOS * \
                                 (2 / (1 + p.PONDERADOR_DIFICULTAD)) ** self.nivel
        self.tiempo = 0
        self.iniciar_nivel()

    def detener_juego(self):
        self.timer.stop()
        self.pausa = True

    def reanudar_juego(self):
        self.timer.start()
        self.pausa = False

    def colision(self, lista, objeto):
        for l in lista:
            if l.cuerpo.intersects(objeto):
                return l
        return False

    def manejo_tecla(self, tecla):
        if tecla == 'P':
            if self.pausa:
                self.reanudar_juego()
            else:
                self.detener_juego()
        if tecla in 'vidn':
            self.cheatcode.append(tecla)
        if tecla in 'UD':
            if not self.colision(self.troncos, objeto=self.sapo.cuerpo):
                self.avanzar.append(tecla)
            self.sapo.direccion = tecla
        if tecla in 'RL':
            self.sapo.direccion = tecla
            if self.movimiento_en_tronco(self.sapo, tecla):
                self.avanzar.append(tecla)
        if self.colision(self.troncos, objeto=self.sapo.cuerpo):
            if tecla == 'J':
                if self.sapo.direccion in 'RL':
                    self.sapo.avanzar(direccion=self.sapo.direccion,
                                      velocidad=p.PIXELES_SALTO_HORIZONTAL)
                elif self.sapo.direccion in 'UD':
                    self.sapo.avanzar(direccion=self.sapo.direccion,
                                      velocidad=p.PIXELES_SALTO_VERTICAL)

    def timer_tick(self):
        self.tiempo += 1/p.FPS
        if self.sapo.cuerpo.y() < p.Y_WIN:
            self.nivel_superado()
        if self.sapo.cuerpo.y() < p.Y_CHECKPOINT:
            self.check_point = True
        if not self.mapa:
            self.generar_mapa()
        if not self.autos:
            self.generar_auto()
        if not self.troncos:
            self.generar_tronco()
        if self.tiempo % p.TIEMPO_OBJETO == 0:
            self.generar_item()
        if self.tiempo % p.TIEMPO_AUTOS == 0:
            self.generar_auto()
        if self.tiempo % p.TIEMPO_TRONCOS == 0:
            self.generar_tronco()
        if ('v' in self.cheatcode) and ('i' in self.cheatcode) and ('d' in self.cheatcode):
            if 'n' not in self.cheatcode:
                self.sapo.vidas += p.VIDAS_TRAMPA
        if ('n' in self.cheatcode) and ('i' in self.cheatcode) and ('v' in self.cheatcode):
            if 'd' not in self.cheatcode:
                self.post_nivel = True
                self.nivel_superado(superado=True)
        self.cheatcode = []
        anterior = ''
        for a in self.avanzar:
            if a != anterior:
                self.sapo.avanzar(direccion=a)
            anterior = a
        self.avanzar = []

        for a in self.autos:
            a.avanzar(direccion=a.direccion)
        for t in self.troncos:
            t.avanzar(direccion=t.direccion)

        tronco = self.colision(self.troncos, objeto=self.sapo.cuerpo)
        if tronco:
            self.sapo.cuerpo.moveTo(self.sapo.cuerpo.x(), tronco.cuerpo.y())
            self.sapo.avanzar(direccion=tronco.direccion, velocidad=tronco.velocidad)
        item_agarrado = self.colision(self.items, objeto=self.sapo.cuerpo)
        if item_agarrado:
            self.consumir_item(item_agarrado)
            self.items.remove(item_agarrado)
            self.senal_item_agarrado.emit(item_agarrado.numero)
        self.colision_con_bordes(self.sapo)
        if self.colision(self.autos, objeto=self.sapo.cuerpo) or self.colision_rio(self.sapo):
            if not self.check_point:
                self.sapo.cuerpo.moveTo(p.X_INICIAL, p.Y_INICIAL)
            else:
                self.sapo.cuerpo.moveTo(p.X_INICIAL, p.Y_CHECKPOINT)
            self.sapo.vidas -= 1
        if self.sapo.vidas == 0:
            self.nivel_superado(superado=False)
        self.senal_actualizar.emit({
            "sapo": self.sapo,
            "autos": self.autos,  # una lista
            "troncos": self.troncos,  # una lista
            "items": self.items,  # una lista
            "tiempo": self.tiempo_max - self.tiempo,
            "mapa": self.mapa,
            "puntaje": self.puntaje,
            "nivel superado": self.post_nivel
        })

    def generar_mapa(self):
        mapa = random.choice(self.mapas)
        for m in mapa:
            direcciones = random.choice(self.posibles_direcciones)
            self.mapa.append([m, direcciones])

    def generar_auto(self):
        for i, m in enumerate(self.mapa):
            if m[0] == 'C':
                y_inicial = random.choice(p.Y_INICIAL_POSIBLES[i])
                numero = p.Y_INICIAL_POSIBLES[i].index(y_inicial)
                direccion = m[1][numero]
                x_inicial = p.X_INICIAL_POSIBLES[direccion]
                x_inicial -= p.WIDTH_AUTO
                car = Auto(x_inicial, y_inicial, p.WIDTH_AUTO,
                     p.HEIGHT_AUTO, direccion=direccion, velocidad=self.velocidad_autos)
                self.autos.append(car)

    def generar_tronco(self):
        for i, m in enumerate(self.mapa):
            if m[0] == 'R':  # R de rio
                y_inicial = random.choice(p.Y_INICIAL_POSIBLES[i])
                numero = p.Y_INICIAL_POSIBLES[i].index(y_inicial)
                direccion = m[1][numero]
                x_inicial = p.X_INICIAL_POSIBLES[direccion]
                x_inicial -= p.WIDTH_TRONCO
                log = Tronco(x_inicial, y_inicial, p.WIDTH_TRONCO,
                             p.HEIGHT_TRONCO, direccion=direccion, velocidad=self.velocidad_troncos)
                self.troncos.append(log)

    def generar_item(self):
        pos_x = random.choice(list(range(p.MIN_X, p.MAX_X, p.DELTA_MINIMO)))
        pos_y = random.choice(list(range(p.MIN_Y, p.MAX_Y, p.DELTA_MINIMO)))
        tipo = random.choice(p.TIPOS)
        self.items.append(Item(pos_x, pos_y, p.WIDTH_ITEM, p.HEIGHT_ITEM, tipo))

    def consumir_item(self, i):
        if i.tipo == 'moneda':
            self.sapo.monedas += 10
        if i.tipo == 'corazon':
            self.sapo.vidas += 1
        if i.tipo == 'reloj':
            self.tiempo_max += 10 * (self.tiempo_max - self.tiempo) / self.tiempo_max
        if i.tipo == 'calavera':
            for t in self.troncos:
                t.velocidad *= 1.05

    def colision_rio(self, sapo):
        if not self.colision(self.troncos, objeto=self.sapo.cuerpo):
            posibilidades = []
            for i, m in enumerate(self.mapa):
                if m[0] == 'R':
                    posibilidades.append(i)
            y_posibles = []
            for n in posibilidades:
                y_posibles.extend(p.Y_INICIAL_POSIBLES[n])
            if sapo.cuerpo.y() in y_posibles:
                return True

    def colision_con_bordes(self, o):
        if o.cuerpo.x() < p.MIN_X:
            o.cuerpo.moveTo(p.MIN_X, o.cuerpo.y())
        if o.cuerpo.x() > p.MAX_X:
            o.cuerpo.moveTo(p.MAX_X, o.cuerpo.y())
        if o.cuerpo.y() < p.MIN_Y:
            o.cuerpo.moveTo(o.cuerpo.x(), p.MIN_Y)
        if o.cuerpo.y() > p.MAX_Y:
            o.cuerpo.moveTo(o.cuerpo.x(), p.MAX_Y)

    def movimiento_en_tronco(self, o, direccion):
        tronco = self.colision(self.troncos, objeto=o.cuerpo)
        if tronco:
            if direccion == 'L':
                if o.cuerpo.x() - 40 <= tronco.cuerpo.x():
                    o.cuerpo.moveTo(tronco.cuerpo.x(), o.cuerpo.y())
                    return False
            if direccion == 'R':
                if o.cuerpo.x() + 40 >= tronco.cuerpo.x() + tronco.cuerpo.width() - o.cuerpo.width():
                    o.cuerpo.moveTo(tronco.cuerpo.x() + tronco.cuerpo.width() - o.cuerpo.width(),
                                    o.cuerpo.y())
                    return False
        return True

    def nivel_superado(self, superado=True):
        puntaje_ronda = int((self.sapo.vidas * 100 + (self.tiempo_max - self.tiempo) * 50)
                            * self.nivel)
        self.puntaje += puntaje_ronda
        dic = {
            "nivel": self.nivel,
            "puntaje total": self.puntaje,
            "puntaje ronda": puntaje_ronda,
            "sapo": self.sapo,
            "nivel superado": superado
        }
        self.detener_juego()
        self.senal_avanzar_nivel.emit(dic)
        self.post_nivel = True


class Objeto(QObject):
    def __init__(self, pos_x, pos_y, ancho, altura, direccion=''):
        super().__init__()
        self.direccion = direccion
        self.cuerpo = QRect(pos_x, pos_y, ancho, altura)
        self.velocidad = 0

    def avanzar(self, direccion, velocidad=False):
        if not velocidad:
            velocidad = self.velocidad
        delta = (0, 0)
        if direccion == "R":
            delta = (velocidad, 0)
        elif direccion == "L":
            delta = (-1 * velocidad, 0)
        elif direccion == "U":
            delta = (0, -1 * velocidad)
        elif direccion == 'D':
            delta = (0, velocidad)
        self.cuerpo = self.cuerpo.translated(*delta)


class Sapo(Objeto):
    def __init__(self, pos_x, pos_y, ancho, altura, direccion):
        super().__init__(pos_x, pos_y, ancho, altura, direccion)
        self.__vidas = p.VIDAS_INICIO
        self.monedas = 0
        self.velocidad = p.VELOCIDAD_CAMINAR
        self.nombre = ''

    def definir_nombre(self, n):
        self.nombre = n

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, v):
        if v > 12:
            self.__vidas = 12
        elif v < 0:
            self.__vidas = 0
        else:
            self.__vidas = v


class Auto(Objeto):
    id_ = 0  # Id único para cada instancia de Auto

    def __init__(self, pos_x, pos_y, ancho, altura, direccion, velocidad):
        super().__init__(pos_x, pos_y, ancho, altura, direccion)
        self.velocidad = velocidad
        self.numero = str(Auto.id_)
        Auto.id_ += 1


class Tronco(Objeto):
    id_ = 0

    def __init__(self, pos_x, pos_y, ancho, altura, direccion, velocidad):
        super().__init__(pos_x, pos_y, ancho, altura, direccion)
        self.velocidad = velocidad
        self.numero = str(Tronco.id_)
        Tronco.id_ += 1


class Item(Objeto):
    id_ = 0

    def __init__(self, pos_x, pos_y, ancho, altura, tipo):
        super().__init__(pos_x, pos_y, ancho, altura)
        self.tipo = tipo
        self.numero = str(Item.id_)
        Item.id_ += 1
