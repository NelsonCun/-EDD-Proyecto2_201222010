from src.structs.listaSimple.NodoListaSimple import NodoListaSimple

class ListaSimple:
    
    def __init__(self):
        self.__cabeza = None
        self.size = 0
        
    def insertar(self, valor)->None:
        nuevo = NodoListaSimple(valor)
        if self.size == 0:
            self.cabeza = nuevo
            return
        else:
            nuevo.setSiguiente(self.cabeza)
            self.cabeza = nuevo
        self.size += 1
        
    def getCabeza(self):
        return self.__cabeza