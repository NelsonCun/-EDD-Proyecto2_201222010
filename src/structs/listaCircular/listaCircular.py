from .nodoListaCircular import nodoListaCircular
from src.classes.cliente import cliente
import os

class listaCircular:
    
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0
        
    def getInicio(self) -> nodoListaCircular:
        return self.inicio
    
    def setInicio(self, inicio):
        self.inicio = inicio
        
    def getFinal(self) -> nodoListaCircular :
        return self.final
    
    def setFinal(self, final):
        self.final = final
        
    def getSize(self) -> int:
        return self.size
    
    def insertar(self, cliente: cliente):
        nuevo = nodoListaCircular(cliente)
        if self.inicio == None:
            self.inicio = nuevo
            self.final = nuevo
            self.inicio.setSiguiente(self.inicio)
            self.inicio.setAnterior(self.inicio)
        elif cliente.getDpi() < self.inicio.getCliente().getDpi():
            nuevo.setSiguiente(self.inicio)
            nuevo.setAnterior(self.final)
            self.final.setSiguiente(nuevo)
            self.inicio.setAnterior(nuevo)
            self.inicio = nuevo
        elif cliente.getDpi() > self.final.getCliente().getDpi():
            nuevo.setSiguiente(self.inicio)
            nuevo.setAnterior(self.final)
            self.final.setSiguiente(nuevo)
            self.inicio.setAnterior(nuevo)
            self.final = nuevo
        else:
            aux = self.inicio
            while aux.getSiguiente() != self.inicio:
                if cliente.getDpi() < aux.getSiguiente().getCliente().getDpi():
                    nuevo.setSiguiente(aux.getSiguiente())
                    nuevo.setAnterior(aux)
                    aux.getSiguiente().setAnterior(nuevo)
                    aux.setSiguiente(nuevo)
                    break
                aux = aux.getSiguiente()
        self.size += 1
        print(f"Cliente {cliente.getDpi()}, nombre {cliente.getNombres()} insertado exitosamente.")
        
    def modificar(self, dpi: int):
        nodo_cliente = self.buscar(dpi)
        if nodo_cliente!= None:
            cliente = nodo_cliente.getCliente()
            print("Ingrese los nuevos datos del cliente:")
            cliente.setNombres(input("Nombres: "))
            cliente.setApellidos(input("Apellidos: "))
            cliente.setGenero(input("Genero: "))
            cliente.setTelefono(int(input("Teléfono: ")))
            cliente.setDireccion(input("Dirección: "))
            print("Cliente modificado exitosamente.")
        else:
            print("Cliente no encontrado.")
            
    def eliminar(self, dpi: int):
        if self.inicio == None:
            print("Lista vacía.")
            return
        if self.inicio.getDpi() == dpi:
            self.inicio = self.inicio.getSiguiente()
            self.final.setSiguiente(self.inicio)
            self.inicio.setAnterior(self.final)
            self.size -= 1
            print("Cliente eliminado exitosamente.")
            return
        elif self.final.getDpi() == dpi:
            self.final = self.final.getAnterior()
            self.final.setSiguiente(self.inicio)
            self.inicio.setAnterior(self.final)
            self.size -= 1
            print("Cliente eliminado exitosamente.")
            return
        else:
            aux = self.buscar(dpi)
            if aux != None:
                aux.getAnterior().setSiguiente(aux.getSiguiente())
                aux.getSiguiente().setAnterior(aux.getAnterior())
                self.size -= 1
                print("Cliente eliminado exitosamente.")
                return
        print("Cliente no encontrado.")
        
    def mostrarInformacion(self, dpi: int) -> str:
        cliente = self.buscar(dpi)
        if cliente != None:
            return str(cliente)
        return "Cliente no encontrado."
    
    def buscar(self, dpi: int) -> cliente:
        aux = self.inicio
        if aux is None:  # Si la lista está vacía
            return None
        while True:
            if aux.getCliente().getDpi() == dpi:
                return aux
            aux = aux.getSiguiente()
            if aux == self.inicio:  # Regresaste al inicio
                break
        return None

    
    def mostrarEstructura(self): #utilizar graphiz
        pass