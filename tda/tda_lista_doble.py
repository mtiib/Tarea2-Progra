from models.vuelo import Vuelo

class Nodo:
    def __init__(self, vuelo):
        self.vuelo = vuelo
        self.prev = None
        self.next = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def insertar_al_frente(self, vuelo):
        nuevo = Nodo(vuelo)
        if not self.head:
            self.head = self.tail = nuevo
        else:
            nuevo.next = self.head
            self.head.prev = nuevo
            self.head = nuevo
        self._size += 1

    def insertar_al_final(self, vuelo):
        nuevo = Nodo(vuelo)
        if not self.tail:
            self.head = self.tail = nuevo
        else:
            self.tail.next = nuevo
            nuevo.prev = self.tail
            self.tail = nuevo
        self._size += 1

    def obtener_primero(self):
        return self.head.vuelo if self.head else None

    def obtener_ultimo(self):
        return self.tail.vuelo if self.tail else None

    def longitud(self):
        return self._size

    def insertar_en_posicion(self, vuelo, pos):
        if pos < 0 or pos > self._size:
            raise IndexError("Posición fuera de rango")
        if pos == 0:
            return self.insertar_al_frente(vuelo)
        if pos == self._size:
            return self.insertar_al_final(vuelo)

        nuevo = Nodo(vuelo)
        actual = self.head
        for _ in range(pos):
            actual = actual.next

        anterior = actual.prev
        anterior.next = nuevo
        nuevo.prev = anterior
        nuevo.next = actual
        actual.prev = nuevo
        self._size += 1

    def extraer_de_posicion(self, pos):
        if pos < 0 or pos >= self._size:
            raise IndexError("Posición fuera de rango")
        actual = self.head
        for _ in range(pos):
            actual = actual.next
        if actual.prev:
            actual.prev.next = actual.next
        else:
            self.head = actual.next
        if actual.next:
            actual.next.prev = actual.prev
        else:
            self.tail = actual.prev
        self._size -= 1
        return actual.vuelo