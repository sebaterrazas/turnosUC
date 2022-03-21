from random import randint
from time import sleep
from pedido import Pedido
from shopper import Shopper
from threading import Thread


class DCComidApp(Thread):

    def __init__(self, shoppers, tiendas, pedidos):
        # NO MODIFICAR
        super().__init__()
        self.shoppers = shoppers
        self.pedidos = pedidos
        self.tiendas = tiendas

    def obtener_shopper(self):
        for s in self.shoppers:
            if not s.ocupado:
                return s
        print('Todos shoppers ocupados :(')
        Shopper.evento_disponible.wait()
        print('Se encontró un shopper')
        Shopper.evento_disponible.clear()
        self.obtener_shopper()

    def run(self):
        for p in self.pedidos:
            id_, nombre_tienda, descripcion = p
            tienda = self.tiendas[nombre_tienda]
            pedido = Pedido(int(id_), nombre_tienda, descripcion)
            shopper = self.obtener_shopper()
            shopper.asignar_pedido(pedido)
            tienda.ingresar_pedido(pedido, shopper)
            trafico_aleatorio = randint(1, 5)
            sleep(trafico_aleatorio)


if __name__ == '__main__':
    pass
