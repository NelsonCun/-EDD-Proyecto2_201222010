from src.classes.vehiculo import vehiculo
class NodoArbolB:
    
    def __init__(self, hoja: bool=False):
        self.hoja: bool = hoja
        self.claves: list[vehiculo] = [] # orden del arbol - 1 (m-1) (En el laboratorio debería ser vehículos)
        self.hijos: list[NodoArbolB] = [] # orden del arbol (m)
        
        
    def __str__(self):
        return f"Hoja: {self.hoja} - claves: {self.claves} - hijos: {self.hijos}"