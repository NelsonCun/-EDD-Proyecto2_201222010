from src.structs.listaSimple.listaSimple import ListaSimple
from src.structs.listaSimple.NodoListaSimple import NodoListaSimple
from src.classes.vertice import Vertice
from src.structs.Cola.Cola import Cola
from src.utils.manejadorArchivos import leer_archivo
from src.classes.ruta import ruta
from copy import copy

class listaAdyacencia:
    
    def __init__(self):
        self.vertices: ListaSimple[Vertice] = ListaSimple()
        
    def insertar(self, ruta: ruta):
        vertice: Vertice = self.buscar_vertice(ruta.getOrigen())
        if vertice != None:
            vertice.agregar_vecino(ruta.getDestino(), ruta.getTiempoRuta())
            return
        
        vertice = Vertice(ruta.getOrigen())
        vertice.agregar_vecino(ruta.getDestino(), ruta.getTiempoRuta())
        
        self.vertices.insertar(vertice)
            
    def buscar_vertice(self, valor: str) -> Vertice:
        aux: NodoListaSimple[Vertice] = self.vertices.getCabeza()
    
        while aux != None:
            if aux.getValor().getValorVertice() == valor:
                return aux.getValor()
            aux = aux.getSiguiente()
        return None
    
    def get_ruta(self, origen:str, destino:str) -> ListaSimple:
        ruta: ListaSimple[Vertice] = ListaSimple()
        nodos_visitados: Cola = Cola()
        nodos: Cola = Cola()
        
        