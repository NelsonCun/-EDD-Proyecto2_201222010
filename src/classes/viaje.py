from src.structs.listaAdyacencia.listaAdyacencia import listaAdyacencia
from src.classes.cliente import cliente
from src.classes.vehiculo import vehiculo
from src.structs.listaSimple.listaSimple import ListaSimple
from src.structs.listaSimple.NodoListaSimple import NodoListaSimple
from src.classes.vertice import Vertice
from src.utils.manejadorArchivos import writeFile
import os


class viaje:
    
    def __init__(self, idViaje, lugarOrigen, lugarDestino, fechaInicio, horaInicio, cliente, vehiculo):
        self.__idViaje = idViaje
        self.__lugarOrigen = lugarOrigen
        self.__lugarDestino = lugarDestino
        self.__fechaInicio = fechaInicio
        self.__horaInicio = horaInicio
        self.__cliente = cliente
        self.__vehiculo = vehiculo
        self.__rutaTomada: ListaSimple[Vertice] = None
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
        
    def getRutaTomada(self, grafo: listaAdyacencia):
        self.__rutaTomada = grafo.get_ruta(self.__lugarOrigen, self.__lugarDestino)
    
    def setRutaTomada(self, rutaTomada):
        self.__rutaTomada = rutaTomada
        
    def mostrar_ruta(self) -> str:
        ruta: str = ""
        aux: NodoListaSimple[Vertice] = self.__rutaTomada.getCabeza()
        
        while aux!= None:
            if aux.getValor().get_peso_acumulado() == 0:
                ruta += f"{aux.getValor().getValorVertice()}({aux.getValor().get_peso_acumulado()})->"
            else:
                ruta += f"{aux.getValor().getValorVertice()}({peso}+{aux.getValor().getPesoVertice()})={aux.getValor().get_peso_acumulado()})->"
            
            peso:int = aux.getValor().get_peso_acumulado()
            
            aux = aux.getSiguiente()
        
        return ruta
    
    
    def generar_reporte(self):
        # Generar el archivo DOT
        writeFile('src/images/estructura.dot', self.imprimir())

        # Generar la imagen PNG
        result: int = os.system("dot -Tpng src/images/estructura.dot -o src/images/estructura.png")

        if result == 0:
            print("Reporte generado correctamente en src/images/estructura.png")
            
        
    def imprimir(self) -> str:
        ruta_dot = "digraph G {\n"
        ruta_dot += "    rankdir=LR;\n"
        ruta_dot += "    node [shape=rectangle];\n"
        
        aux = self.__rutaTomada.getCabeza()
        
        while aux != None:
            vertice = aux.getValor()
            if aux.getSiguiente() != None:
                siguiente_vertice = aux.getSiguiente().getValor()
                peso = vertice.get_peso_acumulado()
                ruta_dot += f'    "{vertice.getValorVertice()}" [label="Nombre = {vertice.getValorVertice()}'
                ruta_dot += f'\n Tiempo = {peso}+{siguiente_vertice.getPesoVertice()}={siguiente_vertice.get_peso_acumulado()}'
                ruta_dot += f'"];\n'
                ruta_dot += f'    "{vertice.getValorVertice()}" -> "{siguiente_vertice.getValorVertice()}";\n'
            aux = aux.getSiguiente()

        ruta_dot += "}"
        return ruta_dot
        
        
    def __str__(self):
        print(f"ID Viaje: {self.__idViaje}, Lugar de Origen: {self.__lugarOrigen}, Lugar de Destino: {self.__lugarDestino}, Fecha de Inicio: {self.__fechaInicio}, Hora de Inicio: {self.__horaInicio}, Cliente: {self.__cliente}, Vehículo: {self.__vehiculo}, Ruta Tomada: {self.__rutaTomada}")