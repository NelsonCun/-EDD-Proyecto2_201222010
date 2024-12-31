class NodoListaSimple:
    
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None
        
    def getValor(self):
        return self.__valor
    
    def setValor(self, valor):
        self.__valor = valor
        
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def __str__(self):
        return str