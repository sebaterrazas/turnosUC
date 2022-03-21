from random import choice
import parametros as p


class Tributo:
    def __init__(self, nombre, distrito, edad, vida,
                 energia, agilidad, fuerza, ingenio, popularidad):
        self.nombre = nombre
        self.distrito = distrito
        self.edad = int(edad)
        self._vida = int(vida)
        self._energia = int(energia)
        self.agilidad = int(agilidad)
        self.fuerza = int(fuerza)
        self.ingenio = int(ingenio)
        self.popularidad = int(popularidad)
        self.mochila = []

    @property
    def esta_vivo(self):
        return self.vida > p.VIDA_MIN

    @property
    def peso(self):
        pesos_mochila = map(lambda o: o.peso, self.mochila)
        return sum(pesos_mochila)

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, v):
        if v > 100:
            self._vida = p.VIDA_MAX
        elif v < 0:
            self._vida = p.VIDA_MIN
        else:
            self._vida = v

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, e):
        if e > 100:
            self._energia = p.ENERGIA_MAX
        elif e < 0:
            self._energia = p.ENERGIA_MIN
        else:
            self._energia = e

    def atacar(self, otro):
        ataque = (60 * self.fuerza + 40 * self.agilidad +
                  40 * self.ingenio - 30 * self.peso) / self.edad
        otro.vida -= min(90, max(5, int(ataque)))

    def utilizar_objeto(self, arena, objeto):    # Al utilizar un objeto, este se consume
        objeto.entregar_beneficio(self, arena)   # y 'desaparece' de la mochila.
        self.mochila.remove(objeto)

    def pedir_objeto(self, objetos):  # Al llamar la función, el Tributo ya pagó con popularidad
        objeto = choice(objetos)
        self.mochila.append(objeto)
        return objeto

    def accion_heroica(self):
        self.energia -= p.ENERGIA_ACCION_HEROICA
        self.popularidad += p.POPULARIDAD_ACCION_HEROICA

    def __str__(self):
        return self.nombre

