from src.structs.listaSimple.NodoListaSimple import NodoListaSimple

class ListaSimple:
    
    def __init__(self):
        self.__cabeza = None
        self.size = 0
        
    def insertar(self, valor)->None:
        nuevo = NodoListaSimple(valor)
        if self.size == 0:
            self.__cabeza = nuevo
            self.size += 1
            return
        else:
            nuevo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
            self.size += 1
            return
        
    def getCabeza(self):
        return self.__cabeza
    
    def getSize(self):
        return self.size
    
    def agregar(self,valor)->None:
        nuevo = NodoListaSimple(valor)
        if self.size == 0:
            self.__cabeza = nuevo
            self.size += 1
            return
        else:
            aux = self.__cabeza
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(nuevo)
            self.size += 1
            return