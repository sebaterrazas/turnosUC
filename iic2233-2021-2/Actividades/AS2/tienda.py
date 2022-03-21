from threading import Thread, Lock
from time import sleep
from random import randint


class Tienda(Thread):
    def __init__(self, nombre):
        # NO MODIFICAR
        super().__init__()
        self.nombre = nombre
        self.cola_pedidos = []
        self.abierta = True
        # COMPLETAR DESDE AQUI
        self.lock = Lock()

    def ingresar_pedido(self, pedido, shopper):
        with self.lock:
            self.cola_pedidos.append((pedido, shopper))

    def preparar_pedido(self, pedido):  # Observación, no se utiliza pedido
        tiempo_preparacion = randint(1, 10)
        print('El pedido se demorará', tiempo_preparacion)
        sleep(tiempo_preparacion)
        print('Pedido listo')

    def run(self):
        while self.abierta:
            if self.cola_pedidos:
                with self.lock:
                    pedido, shopper = self.cola_pedidos.pop(0)  # Observación, no se utiliza shopper
                    self.preparar_pedido(pedido)
                    pedido.evento_pedido_listo.set()
                    pedido.evento_llego_repartidor.wait()
            else:
                descanso = randint(1, 5)
                print(f'No hay ningún pedido en {self.nombre}...')
                print('Esperaremos', descanso, 'segundos.')
                sleep(descanso)

