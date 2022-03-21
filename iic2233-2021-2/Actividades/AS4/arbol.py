class NodoFama:

    def __init__(self, usuario, padre=None):
        # No modificar
        self.usuario = usuario
        self.padre = padre
        self.hijo_izquierdo = None
        self.hijo_derecho = None


class ArbolBinario:

    def __init__(self):
        # No modificar
        self.raiz = None

    def crear_arbol(self, nodos_fama):
        # No modificar
        for nodo in nodos_fama:
            self.insertar_nodo(nodo, self.raiz)

    def insertar_nodo(self, nuevo_nodo, padre=None):
        if self.raiz == None or padre == None:
            self.raiz = nuevo_nodo
            return
        if padre.usuario.fama > nuevo_nodo.usuario.fama:
            if padre.hijo_izquierdo == None:
                padre.hijo_izquierdo = nuevo_nodo
            else:
                self.insertar_nodo(nuevo_nodo, padre.hijo_izquierdo)
        if padre.usuario.fama < nuevo_nodo.usuario.fama:
            if padre.hijo_derecho == None:
                padre.hijo_derecho = nuevo_nodo
            else:
                self.insertar_nodo(nuevo_nodo, padre.hijo_derecho)

    def buscar_nodo(self, fama, padre=None):
        # bfs iterativo
        cola = [self.raiz]
        # Mientras queden vertices por visitar y no nos pasemos del limite de navegación
        while len(cola) > 0:
            # Obtenemos de la cola el próximo vertice
            vertice = cola.pop(0)
            # Agregamos los vecinos al stack
            cola.append(vertice.hijo_izquierdo)
            cola.append(vertice.hijo_derecho)
            if vertice:
                if vertice.usuario.fama == fama:
                    return vertice
        return None

    def print_arbol(self, nodo=None, nivel_indentacion=0):
        # No modificar
        indentacion = "|   " * nivel_indentacion
        if nodo is None:
            print("** DCCelebrity Arbol Binario**")
            self.print_arbol(self.raiz)
        else:
            print(f"{indentacion}{nodo.usuario.nombre}: "
                  f"{nodo.usuario.correo}")
            if nodo.hijo_izquierdo:
                self.print_arbol(nodo.hijo_izquierdo,
                                 nivel_indentacion + 1)
            if nodo.hijo_derecho:
                self.print_arbol(nodo.hijo_derecho,
                                 nivel_indentacion + 1)
