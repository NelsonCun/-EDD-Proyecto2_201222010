class ruta:
    
    def __init__(self, origen, destino, tiempoRuta):
        self.__origen = origen
        self.__destino = destino
        self.__tiempoRuta = tiempoRuta
        
    def getOrigen(self) -> str:
        return self.__origen
    
    def setOrigen(self, origen: str) -> None:
        self.__origen = origen
        
    def getDestino(self) -> str:
        return self.__destino
    
    def setDestino(self, destino: str) -> None:
        self.__destino = destino
        
    def getTiempoRuta(self) -> str:
        return self.__tiempoRuta
    
    def setTiempoRuta(self, tiempoRuta: str) -> None:
        self.__tiempoRuta = tiempoRuta
        
    def __str__(self):
        print(f"Origen: {self.__origen}, Destino: {self.__destino}, Tiempo de Ruta: {self.__tiempoRuta}")