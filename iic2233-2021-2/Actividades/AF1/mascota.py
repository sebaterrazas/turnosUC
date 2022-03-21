import random
import parametros as p


class Mascota:
    def __init__(self, nombre, raza, dueno,
                 saciedad, entretencion):
        self.nombre = nombre
        self.raza = raza
        self.dueno = dueno
        
        # Los siguientes valores están en %.
        self._saciedad = int(saciedad)
        self._entretencion = int(entretencion)

    @property
    def saciedad(self):
        return self._saciedad

    @saciedad.setter
    def saciedad(self, s):
        s = int(s)
        if s > 100:
            self._saciedad = 100
        elif s < 0:
            self._saciedad = 0
        else:
            self._saciedad = s

    @property
    def entretencion(self):
        return self._entretencion

    @entretencion.setter
    def entretencion(self, e):
        e = int(e)
        if e > 100:
            self._entretencion = 100
        elif e < 0:
            self._entretencion = 0
        else:
            self._entretencion = e

    @property
    def satisfaccion(self):
        return (self.saciedad//2 + self.entretencion//2)
    
    def comer(self, comida):
        comida_vencida = random.random()
        if comida_vencida < comida.probabilidad_vencer:
            self._saciedad -= comida.calorias
            print(f"La comida estaba vencida! A {self.nombre} le duele la pancita :(")

        else:
            self._saciedad += comida.calorias
            print(f"{self.nombre} está comiendo {comida.nombre}, que rico!")

    def pasear(self):
        self.entretencion += p.ENTRETENCION_PASEAR
        self.saciedad += p.SACIEDAD_PASEAR
    
    def __str__(self):
        string = f'''
Nombre: {self.nombre}
Saciedad: {self._saciedad}
Entretención: {self._entretencion}
Satisfacción: {self.satisfaccion}
'''
        return string


class Perro(Mascota):
    def __init__(self, nombre, raza, dueno,
                 saciedad, entretencion):
        Mascota.__init__(self, nombre, raza, dueno,
                 saciedad, entretencion)
        self.especie = 'PERRO'
    
    def saludar(self):
        print('guau guau')
        

class Gato(Mascota):
    def __init__(self, nombre, raza, dueno,
                 saciedad, entretencion):
        Mascota.__init__(self, nombre, raza, dueno,
                         saciedad, entretencion)
        self.especie = 'GATO'

    def saludar(self):
        print('miau miau')


class Conejo(Mascota):
    def __init__(self, nombre, raza, dueno,
                 saciedad, entretencion):
        Mascota.__init__(self, nombre, raza, dueno,
                         saciedad, entretencion)
        self.especie = 'CONEJO'

    def saludar(self):
        print('hathci hathci hathci ohhh')
