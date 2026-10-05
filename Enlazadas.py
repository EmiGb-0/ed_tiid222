
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            print(f"Agregado: {dato} como cabeza de la lista.")
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            print(f"Agregado: {dato} al final de la lista.")

    def eliminar(self, dato):
        if not self.cabeza:
            print("La lista está vacía. No se puede eliminar.")
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            print(f"Eliminado: {dato} de la cabeza de la lista.")
            return

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente

        if actual.siguiente and actual.siguiente.dato == dato:
            actual.siguiente = actual.siguiente.siguiente
            print(f"Eliminado: {dato} de la lista.")
        else:
            print(f"No se encontró el elemento: {dato} en la lista.")

    def mostrar(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return

        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print("Elementos en la lista:", " -> ".join(elementos))