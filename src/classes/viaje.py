class viaje:
    
    def __init__(self):
        self.__idViaje = None
        self.__lugarOrigen = None
        self.__lugarDestino = None
        self.__fechaInicio = None
        self.__horaInicio = None
        self.__cliente = None
        self.__vehiculo = None
        self.__rutaTomada = None
        
    def getIdViaje(self) -> int:
        return self.__idViaje
    
    def setIdViaje(self, idViaje: int) -> None:
        self.__idViaje = idViaje
        
    def getLugarOrigen(self) -> str:
        return self.__lugarOrigen
    
    def setLugarOrigen(self, lugarOrigen: str) -> None:
        self.__lugarOrigen = lugarOrigen
        
    def getLugarDestino(self) -> str:
        return self.__lugarDestino
    
    def setLugarDestino(self, lugarDestino: str) -> None:
        self.__lugarDestino = lugarDestino
        
    def getFechaInicio(self) -> str:
        return self.__fechaInicio
    
    def setFechaInicio(self, fechaInicio: str) -> None:
        self.__fechaInicio = fechaInicio
        
    def getHoraInicio(self) -> str:
        return self.__horaInicio
    
    def setHoraInicio(self, horaInicio: str) -> None:
        self.__horaInicio = horaInicio
        
    def getCliente(self):
        return self.__cliente
    
    def setCliente(self, cliente):
        self.__cliente = cliente
        
    def getVehiculo(self):
        return self.__vehiculo
    
    def setVehiculo(self, vehiculo):
        self.__vehiculo = vehiculo
        
    def getRutaTomada(self):
        return self.__rutaTomada
    
    def setRutaTomada(self, rutaTomada):
        self.__rutaTomada = rutaTomada
        
    def __str__(self):
        print(f"ID Viaje: {self.__idViaje}, Lugar de Origen: {self.__lugarOrigen}, Lugar de Destino: {self.__lugarDestino}, Fecha de Inicio: {self.__fechaInicio}, Hora de Inicio: {self.__horaInicio}, Cliente: {self.__cliente}, Vehículo: {self.__vehiculo}, Ruta Tomada: {self.__rutaTomada}")