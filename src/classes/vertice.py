from src.structs.listaSimple.listaSimple import ListaSimple
from src.structs.listaSimple.NodoListaSimple import NodoListaSimple

class Vertice:
    
    def __init__(self, valor: str, peso: int=0, padre = None):
        self.__valor: str = valor
        self.__peso: int = peso
        self.__padre: Vertice = padre
        self.__vecinos: ListaSimple[Vertice] = ListaSimple()
        self.__peso_acumulado: int = 0
        
    def agregar_vecino(self, valor: str, peso: int):
        vecino: Vertice = Vertice(valor, peso)
        vecino.set_peso_acumulado(self.__peso)
        
        self.__vecinos.insertar(vecino)
        
    def set_peso_acumulado(self, peso: int):
        self.__peso_acumulado += peso
        
    def get_peso_acumulado(self) -> int:
        return self.__peso_acumulado
    
    def getValorVertice(self):
        return self.__valor
    
    def getPesoVertice(self):
        return self.__peso
    
    def getPadre(self):
        return self.__padre
    
    def getVecinos(self):
        return self.__vecinos
    
    def setValorVertice(self, valor: str):
        self.__valor = valor
        
    def setPesoVertice(self, peso: int):
        self.__peso = peso
        
    def setPadre(self, padre):
        self.__padre = padre