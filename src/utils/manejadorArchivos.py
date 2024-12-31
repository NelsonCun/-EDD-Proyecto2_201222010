def leer_archivo(path:str) -> str:
    
    with open(path, 'r') as file:
        return file.read()
    
def writeFile(ruta: str, contenido: str):
    with open(ruta, "w") as file:
        file.write(contenido)
        
def readFile(ruta: str)->str:
    
    contenido: str
    with open(ruta, "r") as file:
        contenido = file.read()
        
    return contenido