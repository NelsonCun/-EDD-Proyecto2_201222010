from src.structs.Cola.NodoCola import NodoCola
from src.classes.vertice import Vertice

class Cola:
    
    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.size = 0
    
    def encolar(self, valor):
        nuevo = NodoCola(valor)
        if self.size == 0:
            self.__cabeza = nuevo
            self.__cola = nuevo
            self.size += 1
            return
        self.__cola.setSiguiente(nuevo)
        self.__cola = nuevo
        self.size += 1
        
    def desencolar(self) -> NodoCola:
        if self.size == 0:
            return None
        valor = self.__cabeza.getValor()
        self.__cabeza = self.__cabeza.getSiguiente()
        self.size -= 1
        return valor
    
    def ordenar(self):
        if self.size == 0:
            print ("La cola esta vacia")
            return
        actual: NodoCola[Vertice] = self.__cabeza
        
        while actual != None:
            siguiente: NodoCola[Vertice] = actual.getSiguiente()
            
            while siguiente != None:
                if actual.getValor().get_peso_acumulado() > siguiente.getValor().get_peso_acumulado():
                    temp: Vertice = siguiente.getValor()
                    siguiente.setValor(actual.getValor())
                    actual.setValor(temp)
                    
                siguiente = siguiente.getSiguiente()
            
            actual = actual.getSiguiente()
            
    def buscar(self, valor) -> NodoCola:
        aux: NodoCola[Vertice] = self.__cabeza
        while aux != None:
            if aux.getValor().getValorVertice() == valor:
                return aux
            aux = aux.getSiguiente()
        return None