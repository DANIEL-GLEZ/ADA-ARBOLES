class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    def buscaMenor(self):
        if self.raiz is None:
            return None
        return self._buscaMenor(self.raiz)

    def _buscaMenor(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.valor

    def buscaMayor(self):
        if self.raiz is None:
            return None
        return self._buscaMayor(self.raiz)

    def _buscaMayor(self, nodo):
        actual = nodo
        while actual.derecha is not None:
            actual = actual.derecha
        return actual.valor

    def __del__(self):
        self.raiz = None
        print("Árbol destruido")

    def recorrerInOrden(self):
        if not self.esVacio():
            self._recorrerInOrden(self.raiz)
        else:
            print("El árbol está vacío")

    def _recorrerInOrden(self, nodo):
        if nodo is not None:
            self._recorrerInOrden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._recorrerInOrden(nodo.derecha)

arbol = Arbol()
print("El árbol está vacío:", arbol.esVacio())

arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print("El árbol está vacío:", arbol.esVacio())
print("Buscar 3:", arbol.buscar(3))
print("Buscar 9:", arbol.buscar(9))
print("Menor valor en el árbol:", arbol.buscaMenor())
print("Mayor valor en el árbol:", arbol.buscaMayor())

print("Contenido del árbol en orden:")
arbol.recorrerInOrden()

del arbol


