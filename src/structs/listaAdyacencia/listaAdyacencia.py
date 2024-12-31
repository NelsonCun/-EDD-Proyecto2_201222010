from src.structs.listaSimple.listaSimple import ListaSimple
from src.structs.listaSimple.NodoListaSimple import NodoListaSimple
from src.classes.vertice import Vertice
from src.structs.Cola.Cola import Cola
from src.utils.manejadorArchivos import leer_archivo, writeFile, readFile
import os
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
        
        origen: Vertice = copy(self.buscar_vertice(origen))
        
        if origen == None:
            input(f"La ciudad {origen} no existe")
            return
        
        nodos.encolar(origen)
        
        result: Vertice = self.get_ruta_corta(destino, nodos_visitados, nodos)
        
        while result != None:
            ruta.insertar(result)
            result = result.getPadre()
            
        return ruta
        
    def get_ruta_corta(self, destino:str, nodos_visitados:Cola, nodos: Cola) -> Vertice:
        origen: Vertice = nodos.desencolar()
        
        if origen.getValorVertice() == destino:
            nodos_visitados.encolar(origen)
            return origen
        
        aux: NodoListaSimple[Vertice] = origen.getVecinos().getCabeza()
        
        while aux != None:
            if not self.fue_visitado(nodos_visitados, aux.getValor()):
                peso: int = int(aux.getValor().getPesoVertice())
                
                vecino: Vertice = copy(self.buscar_vertice(aux.getValor().getValorVertice()))
                vecino.setPesoVertice(peso)
                vecino.set_peso_acumulado(origen.get_peso_acumulado() + peso)
                vecino.setPadre(origen)
                
                nodos.encolar(vecino)
                
            aux = aux.getSiguiente()
        
        nodos.ordenar()
        
        nodos_visitados.encolar(origen)
        
        return self.get_ruta_corta(destino, nodos_visitados, nodos)
        
    
    def fue_visitado(self, nodos_visitados: Cola, valor: Vertice) -> bool:
        resultado: NodoListaSimple = nodos_visitados.buscar(valor.getValorVertice())
        return resultado != None
    
    def generar_reporte(self):
        # Generar el archivo DOT
        writeFile('src/images/mapa.dot', self.imprimir())

        # Generar la imagen PNG con mayor resolución (DPI ajustado a 300)
        result: int = os.system("neato -Tpng -Gdpi=300 src/images/mapa.dot -o src/images/mapa.png")

        if result == 0:
            print("Reporte generado correctamente en src/images/mapa.png")
        
    def imprimir(self) -> str:
        # Cabecera del archivo DOT
        dot = 'digraph G {\n\tbgcolor="#1a1a1a"\n\tedge [arrowhead=none fontcolor=white color="#ff5400"];\n\t'
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style=filled fillcolor="#313638" fontcolor=white'
        dot += ' color=transparent];\n\t'

        aux: NodoListaSimple[Vertice] = self.vertices.getCabeza()
        conexiones_impresas = set() 

        while aux is not None:
            vertice: Vertice = aux.getValor()
            vecinos: NodoListaSimple[Vertice] = vertice.getVecinos().getCabeza()

            while vecinos is not None:
                origen = vertice.getValorVertice()
                destino = vecinos.getValor().getValorVertice()

                if (origen, destino) not in conexiones_impresas and (destino, origen) not in conexiones_impresas:
                    dot += f'\t"{origen}" -> "{destino}" [label="{vecinos.getValor().getPesoVertice()}", fontsize=8];\n'
                    conexiones_impresas.add((origen, destino))  # Agregar la conexión al conjunto

                vecinos = vecinos.getSiguiente()
            
            aux = aux.getSiguiente()

        dot += '}'
        return dot