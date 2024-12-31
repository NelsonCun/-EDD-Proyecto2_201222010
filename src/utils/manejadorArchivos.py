def leer_archivo(path:str) -> str:
    
    with open(path, 'r') as file:
        return file.read()