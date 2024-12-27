class cliente:
    def __init__(self, dpi, nombres, apellidos, genero, telefono, direccion):
        self.__dpi= dpi
        self.__nombres= nombres
        self.__apellidos= apellidos
        self.__genero= genero
        self.__telefono= telefono
        self.__direccion= direccion
        
    def getDpi(self) -> int:
        return self.__dpi
    
    def setDpi(self, dpi: int) -> None:
        self.__dpi = dpi
    
    def getNombres(self) -> str:
        return self.__nombres
    
    def setNombres(self, nombres: str) -> None:
        self.__nombres = nombres
    
    def getApellidos(self) -> str:
        return self.__apellidos
    
    def setApellidos(self, apellidos: str) -> None:
        self.__apellidos = apellidos
    
    def getGenero(self) -> chr:
        return self.__genero
    
    def setGenero(self, genero: chr):
        self.__genero = genero
    
    def getTelefono(self) -> int:
        return self.__telefono
    
    def setTelefono(self, telefono: int):
        self.__telefono = telefono
    
    def getDireccion(self) -> str:
        return self.__direccion
    
    def setDireccion(self, direccion: str):
        self.__direccion = direccion
        
    def __str__(self):
        return f"DPI: {self.__dpi}, Nombres: {self.__nombres}, Apellidos: {self.__apellidos}, Genero: {self.__genero}, Teléfono: {self.__telefono}, Dirección: {self.__direccion}"