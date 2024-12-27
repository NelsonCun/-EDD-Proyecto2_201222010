from src.classes.vehiculo import vehiculo
from .NodoArbolB import NodoArbolB
import subprocess

class ArbolB:
    # Constructor
    def __init__(self, orden:int): # Ese es el orden y lo definimos nosotros
        self.raiz: NodoArbolB = NodoArbolB(True)
        self.orden: int = orden
    
    def insertar_valor(self, vehiculo: vehiculo):
        raiz: NodoArbolB = self.raiz
        self.insertar_valor_no_completo(raiz, vehiculo)
        if len(raiz.claves) > self.orden - 1:
            nodo: NodoArbolB = NodoArbolB(False)
            self.raiz = nodo
            nodo.hijos.insert(0, raiz)
            self.dividir_pagina(nodo, 0)
                
    def insertar_valor_no_completo(self, raiz: NodoArbolB, vehiculo: vehiculo):
        posicion: int = len(raiz.claves) - 1 
        if (raiz.hoja):
            #[5, 6]
            raiz.claves.append(None) #Le agrega un espacio a la lista de claves al finally
            #[5, 6, None]
            
            while posicion>=0 and vehiculo.getPlaca()<raiz.claves[posicion].getPlaca():
                raiz.claves[posicion+1] = raiz.claves[posicion]
                #[5, None, 6]
                posicion -= 1
            raiz.claves[posicion+1] = vehiculo #[4, 5, 6]
        else:
            while posicion>=0 and vehiculo.getPlaca()<raiz.claves[posicion].getPlaca():
                posicion -= 1
            posicion += 1
            
            self.insertar_valor_no_completo(raiz.hijos[posicion], vehiculo)
            if (len(raiz.hijos[posicion].claves)) > self.orden -1:
                self.dividir_pagina(raiz, posicion)
    
    def dividir_pagina(self, raiz: NodoArbolB, posicion: int):
        posicion_media: int = int((self.orden-1)/2)
        
        hijo: NodoArbolB = raiz.hijos[posicion]
        nodo: NodoArbolB = NodoArbolB(hijo.hoja)
        
        raiz.hijos.insert(posicion+1, nodo)
        
        raiz.claves.insert(posicion, hijo.claves[posicion_media])
        
        nodo.claves = hijo.claves[posicion_media+1:posicion_media*2+1]
        hijo.claves = hijo.claves[0:posicion_media]
        
        if not hijo.hoja:
            nodo.hijos = hijo.hijos[posicion_media+1:posicion_media*2+2]
            hijo.hijos = hijo.hijos[0:posicion_media+1]
    
    
    def imprimir_usuario(self) -> str:
        
        dot: str = 'Digraph G {\n\tbgcolor="#1A1A1A";\n\t'
        dot += "fontcolor=white;\n\tnodesep=0.5;\n\tsplines=false;\n\t"
        dot += 'node[shape=record whidt=1.2 style=filled fillcolor="#313638" '
        dot += 'fontcolor=white color=transparent];\n\t'
        dot += 'edge [fontcolor=white color="#0070c9"];\n\t'
        
        dot += self.imprimir(self.raiz)
        
        dot += "\n}"
        
        return dot
    
            
    def imprimir(self, nodo: NodoArbolB, id: list[int]=[0]) -> str:
        raiz: NodoArbolB = nodo
        
        arbol = f'n{id[0]}[label="'
        contador: int = 0
        
        for item in raiz.claves:
            if (contador == len(raiz.claves) - 1):
                arbol += f"<f{contador}>|{item.getPlaca()}|<f{contador+1}>"
                break
            arbol += f"<f{contador}>|{item.getPlaca()}|"
            contador += 1
        arbol += "\"];\n\t"
        
        contador: int = 0
        id_padre = id[0]
        for item in raiz.hijos:
            arbol += f'n{id_padre}:f{contador} -> n{id[0] + 1};\n\t'
            id[0] += 1
            arbol+=self.imprimir(item, id)
            
            contador += 1
            
        return arbol
    
    def mostrar_estructura(self):
        contenido_dot = self.imprimir_usuario()
        print (contenido_dot)

        with open("src/images/estructura.dot", "w") as file:
            file.write(contenido_dot)
            
        try:
            subprocess.run(["dot", "-Tpng", "src/images/estructura.dot", "-o", "src/images/estructura.png"], check=True)
            print(f"Imagen generada exitosamente: estructura.png")
        except Exception as e:
            print(f"Error al generar o abrir la imagen: {e}")
            
            
    def buscar_vehiculo(self, placa: str) -> vehiculo:
        return self.buscar(self.raiz, placa)


    def buscar(self, nodo: NodoArbolB, placa: str) -> vehiculo:
        contador = 0
        while contador < len(nodo.claves) and placa > nodo.claves[contador].getPlaca():
            contador += 1

        if contador < len(nodo.claves) and nodo.claves[contador].getPlaca() == placa:
            return nodo.claves[contador]

        if nodo.hoja:
            return None

        return self.buscar(nodo.hijos[contador], placa)

            
    
    def __str__(self):
        return f"{self.raiz}"