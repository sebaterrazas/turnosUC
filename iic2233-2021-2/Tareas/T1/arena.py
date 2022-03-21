import parametros as p
from random import choice, random


class Arena:
    def __init__(self, nombre, dificultad, riesgo, jugador, tributos, ambientes):
        self.nombre = nombre
        self.riesgo = float(riesgo)
        self.dificultad = dificultad
        self.jugador = jugador
        self.tributos = tributos  # Lista de tributos rivales con vida
        self.ambientes = ambientes  # Lista con ambientes en orden

    def ejecutar_evento(self):
        ambiente_actual = self.ambientes.pop(0)  # Elegimos al primer ambiente de la lista
        print()
        print(ambiente_actual, 'es el ambiente actual.')
        self.ambientes.append(ambiente_actual)  # Lo agregamos al final para que sea cíclico
        evento = choice(list(ambiente_actual.eventos)) # Se elige un evento random del ambiente

        ocurrio_evento = p.PROBABILIDAD_EVENTO >= random()  # random tiene como rango [0, 1)
        if ocurrio_evento:
            dano = ambiente_actual.calcular_dano(evento)
            print(f'¡Ha ocurrido un {evento}, dañando a todos en {dano} HP!')
            return dano
        return 0

    def encuentros(self):   # Tributos restantes = Jugador + el resto vivo
        n_encuentros = int(self.riesgo * (len(self.tributos) + 1) // 2)
        batallas = 0
        while batallas <= n_encuentros and self.tributos and self.jugador.esta_vivo:
            atacante = choice(self.tributos)

            posibles_victimas = list(filter(lambda x: x != atacante, self.tributos))
            posibles_victimas.append(self.jugador)
            defensor = choice(posibles_victimas)
            dano = defensor.vida
            atacante.atacar(defensor)
            dano -= defensor.vida
            batallas += 1
            print(f'¡{atacante} ha atacado a {defensor}, quitándole {dano} HP!')
            for t in self.tributos:  # actualizar_tributos
                if not t.esta_vivo:
                    self.tributos.remove(t)
