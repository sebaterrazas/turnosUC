from abc import ABC, abstractmethod
import parametros as p


# Recuerda definir esta clase como abstracta!
class Atraccion(ABC):

    def __init__(self, nombre, capacidad):
        # No modificar
        self.nombre = nombre
        self.capacidad_maxima = capacidad
        self.fila = []

    def ingresar_persona(self, persona):
        # No modificar
        print(f"** {persona.nombre} ha entrado a la fila de {self.nombre}")
        self.fila.append(persona)
        persona.esperando = True

    def nueva_ronda(self):
        # No modificar
        personas_ingresadas = 0
        lista_personas = []
        while personas_ingresadas < self.capacidad_maxima and self.fila:
            lista_personas.append(self.fila.pop(0))

        self.iniciar_juego(lista_personas)

        for persona in lista_personas:
            persona.actuar()

    def iniciar_juego(self, personas):
        # No modificar
        for persona in personas:
            print(f"*** {persona.nombre} jugó esta ronda")
            persona.esperando = False
            self.efecto_atraccion(persona)
        print()

    @abstractmethod
    def efecto_atraccion(self, persona):
        # No modificar
        pass

    def __str__(self):
        return f"Atraccion {self.nombre}"


# Recuerda completar la herencia!
class AtraccionFamiliar(Atraccion):

    def __init__(self, *args):
        super().__init__(*args)
        self.efecto_salud = p.SALUD_FAMILIA
        self.efecto_felicidad = p.FELICIDAD_FAMILIA

    def efecto_atraccion(self, persona):
        persona.felicidad += self.efecto_felicidad
        persona.salud -= self.efecto_salud


# Recuerda completar la herencia!
class AtraccionAdrenalinica(Atraccion):

    def __init__(self, *args):
        super().__init__(*args[:-1])
        self.salud_necesaria = args[-1]
        self.efecto_salud = p.SALUD_ADRENALINA
        self.efecto_felicidad = p.FELICIDAD_ADRENALINA

    def efecto_atraccion(self, persona):
        if self.salud_necesaria > persona.salud:
            print('Bájate bro, te va a dar un paro en este juego')
            persona.salud += int(self.efecto_salud/2)
            persona.felicidad -= int(self.efecto_felicidad/2)
        else:
            persona.salud -= self.efecto_salud
            persona.felicidad += self.efecto_felicidad


# Recuerda completar la herencia!
class AtraccionAcuatica(AtraccionFamiliar):

    def __init__(self, *args):
        super().__init__(*args)
        self.efecto_felicidad = p.FELICIDAD_ACUATICA

    def ingresar_persona(self, persona):
        if persona.tiene_pase:
            super().ingresar_persona(persona)


# Recuerda completar la herencia!
class MontanaAcuatica(AtraccionAdrenalinica, AtraccionAcuatica):

    def __init__(self, *args):
        # nombre=nombre, capacidad=capacidad, salud_necesaria=salud_necesaria, dificultad=dificultad
        super().__init__(*args[:-1])
        self.dificultad = args[-1]

    def iniciar_juego(self, personas):
        for p in personas:
            print(f'{p.nombre} está jugando MontanaAcuatica')
            p.esperando = False
            if p.salud <= self.salud_necesaria * self.dificultad:
                print('¡Hombre al agua!')
                p.tiene_pase = False
            super().efecto_atraccion(p)

