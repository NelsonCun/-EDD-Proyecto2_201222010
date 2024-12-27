class vehiculo:
    
    def __init__(self):
        self.__placa = None
        self.__marca = None
        self.__modelo = None
        self.__precioSegundo = None
        
    def getPlaca(self) -> str:
        return self.__placa
    
    def setPlaca(self, placa: str) -> None:
        self.__placa = placa
        
    def getMarca(self) -> str:
        return self.__marca
    
    def setMarca(self, marca: str) -> None:
        self.__marca = marca
        
    def getModelo(self) -> str:
        return self.__modelo
    
    def setModelo(self, modelo: str) -> None:
        self.__modelo = modelo
        
    def getPrecioSegundo(self) -> float:
        return self.__precioSegundo
    
    def setPrecioSegundo(self, precioSegundo: float) -> None:
        self.__precioSegundo = precioSegundo
        
    def __str__(self):
        print(f"Placa: {self.__placa}, Marca: {self.__marca}, Modelo: {self.__modelo}, Precio por Segundo: {self.__precioSegundo}")