from collections import deque


class NodoGrafo:
    def __init__(self, usuario):
        # No modificar
        self.usuario = usuario
        self.amistades = None

    def formar_amistad(self, nueva_amistad):
        if not self.amistades:
            self.amistades = []
        if not nueva_amistad.amistades:
            nueva_amistad.amistades = []

        if nueva_amistad not in self.amistades:
            self.amistades.append(nueva_amistad)
        if self not in nueva_amistad.amistades:
            nueva_amistad.amistades.append(self)

    def eliminar_amistad(self, ex_amistad):
        if not self.amistades:
            return
        if not ex_amistad.amistades:
            return
        if ex_amistad in self.amistades:
            self.amistades.remove(ex_amistad)
        if self in ex_amistad.amistades:
            ex_amistad.amistades.remove(self)


def recomendar_amistades(nodo_inicial, profundidad):
    # bfs iterado
    # La cola de siempre, comienza desde el nodo inicio.
    cola = deque([nodo_inicial])
    amigos_recomendados = set()

    # Mientras queden vertices por visitar y no nos pasemos del limite de navegación
    while len(cola) > 0 and profundidad > 0:
        # Obtenemos de la cola el próximo vertice
        vertice = cola.popleft()
        # Agregamos los amigos al stack
        if vertice.amistades:
            for amigo in vertice.amistades:
                cola.append(amigo)
                if nodo_inicial.amistades:
                    if amigo not in nodo_inicial.amistades:
                        amigos_recomendados.add(amigo)
        # Visitamos un nodo, bajamos el límite en 1
        profundidad -= 1
    return list(amigos_recomendados)


def busqueda_famosos(nodo_inicial, visitados=None, distancia_min=80):
    """
    [BONUS]
    Recibe un NodoGrafo y busca en la red social al famoso mas
    cercano, retorna la distancia y el nodo del grafo que contiene
    a el usuario famoso cercano al que se encuentra.
    """
    # Completar para el bonus
