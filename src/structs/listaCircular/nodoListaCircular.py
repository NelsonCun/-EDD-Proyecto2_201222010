from src.classes.cliente import cliente
class nodoListaCircular:
    
    def __init__(self, cliente: cliente):
        self.__cliente = cliente
        self.__siguiente = None
        self.__anterior = None
        
    def getCliente(self) -> cliente:
        return self.__cliente
    
    def setCliente(self, cliente):
        self.__cliente = cliente
        
    def getSiguiente(self) -> cliente:
        return self.__siguiente
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
        
    def getAnterior(self) -> cliente:
        return self.__anterior
    
    def setAnterior(self, anterior):
        self.__anterior = anterior
        
    def __str__(self):
        return str(self.__cliente)
        