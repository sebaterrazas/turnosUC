import parametros as p
from abc import ABC, abstractmethod


class Objeto(ABC):
    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.peso = int(peso)
        self.tipo = tipo

    @abstractmethod
    def entregar_beneficio(self, tributo, arena):
        pass


class Arma(Objeto):
    def __init__(self, *args):
        super().__init__(*args)

    def entregar_beneficio(self, tributo, arena):
        super().entregar_beneficio(tributo, arena)
        fuerza_anterior = tributo.fuerza
        tributo.fuerza += tributo.fuerza * int((p.PONDERADOR_AUMENTAR_FUERZA * arena.riesgo + 1))
        print('Tu fuerza aumentó en', tributo.fuerza - fuerza_anterior)

    def __str__(self):
        return f'El arma {self.nombre}'


class Consumible(Objeto):
    def __init__(self, *args):
        super().__init__(*args)

    def entregar_beneficio(self, tributo, arena):
        super().entregar_beneficio(tributo, arena)
        tributo.energia += p.AUMENTAR_ENERGIA
        print('Tu energía aumentó en', p.AUMENTAR_ENERGIA)

    def __str__(self):
        return f'El consumible {self.nombre}'


class Especial(Consumible, Arma):
    def __init__(self, *args):
        super().__init__(*args)

    def entregar_beneficio(self, tributo, arena):
        super().entregar_beneficio(tributo, arena)
        tributo.agilidad += p.AUMENTAR_AGILIDAD
        tributo.ingenio += p.AUMENTAR_INGENIO
        print('Tu agilidad aumentó en', p.AUMENTAR_AGILIDAD)
        print('Tu ingenio aumentó en', p.AUMENTAR_INGENIO)

    def __str__(self):
        return f'El objeto especial {self.nombre}'
