import parametros as p
from abc import ABC, abstractmethod


class Ambiente(ABC):
    def __init__(self, nombre, d_eventos):
        self.nombre = nombre
        self.dano_eventos = d_eventos  # diccionario {evento: int(daño del evento)}
        self.eventos = list(d_eventos)  # lista con llaves del diccionario
        self.humedad = 0
        self.vientos = 0
        self.precipitaciones = 0
        self.nubosidad = 0

    @abstractmethod
    def calcular_dano(self, evento):
        dano = (0.4 * self.humedad + 0.2 * self.vientos + 0.1 * self.precipitaciones
                + 0.3 * self.nubosidad + self.dano_eventos[evento]) / 5
        return max(5, int(dano))


class Playa(Ambiente):
    def __init__(self, *args):
        super().__init__(*args)
        self.humedad = p.HUMEDAD_PLAYA
        self.vientos = p.VELOCIDAD_VIENTOS_PLAYA

    def calcular_dano(self, evento):
        return super().calcular_dano(evento)

    def __str__(self):
        return 'La playa'


class Montana(Ambiente):
    def __init__(self, *args):
        super().__init__(*args)
        self.precipitaciones = p.PRECIPITACIONES_MONTANA
        self.nubosidad = p.NUBOSIDAD_MONTANA

    def calcular_dano(self, evento):
        return super().calcular_dano(evento)

    def __str__(self):
        return 'La montaña'


class Bosque(Ambiente):
    def __init__(self, *args):
        super().__init__(*args)
        self.vientos = p.VELOCIDAD_VIENTOS_BOSQUE
        self.precipitaciones = p.PRECIPITACIONES_BOSQUE

    def calcular_dano(self, evento):
        return super().calcular_dano(evento)

    def __str__(self):
        return 'El bosque'
