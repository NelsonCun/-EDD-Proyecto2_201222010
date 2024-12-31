from src.structs.listaCircular.listaCircular import listaCircular
from src.classes.cliente import cliente
from src.structs.listaCircular.nodoListaCircular import nodoListaCircular
from src.structs.arbolB.arbolB import ArbolB
from src.classes.vehiculo import vehiculo
from src.structs.listaAdyacencia.listaAdyacencia import listaAdyacencia
from src.classes.ruta import ruta
import tkinter as tk
from tkinter import Menu, messagebox, Frame, Label, Button, ttk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

clientes = listaCircular()
vehiculos = ArbolB(5)
destinos = listaAdyacencia()

def reiniciar():
    info_label.place_forget()
    imagen_estructura_label.place_forget()
    
def cargar_clientes_desde_texto(ruta_archivo):
    try:
        with open(ruta_archivo, mode='r') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                # Eliminar los saltos de línea y los espacios extras
                linea = linea.strip().rstrip(';')
                
                if not linea:  # Si la línea está vacía, la ignoramos
                    continue
                
                # Separar los campos por coma y espacio (formato: campo1, campo2, ...)
                campos = [campo.strip() for campo in linea.split(',')]
                
                if len(campos) != 6:
                    messagebox.showerror("Error", f"Formato incorrecto en la línea: {linea}")
                    continue
                
                dpi, nombres, apellidos, genero, telefono, direccion = campos
                
                # Validación de los datos
                if not dpi.isdigit():
                    messagebox.showerror("Error", f"DPI inválido: {dpi}")
                    continue
                if not telefono.isdigit():
                    messagebox.showerror("Error", f"Teléfono inválido para el cliente {nombres} {apellidos}")
                    continue
                if genero == "Masculino":
                    genero = "M"
                if genero == "Femenino":
                    genero = "F"
                
                # Crear un nuevo cliente y agregarlo a la lista circular
                nuevo_cliente = cliente(dpi, nombres, apellidos, genero, telefono, direccion)
                clientes.insertar(nuevo_cliente)  # Insertar en la lista circular
                
            messagebox.showinfo("Carga Masiva", "Clientes cargados exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al cargar los clientes: {e}")

def carga_masiva_clientes():
    archivo = askopenfilename(title="Seleccionar archivo de texto", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        cargar_clientes_desde_texto(archivo)
    
def cargar_vehiculos_desde_texto(ruta_archivo):
    try:
        with open(ruta_archivo, mode='r') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                # Eliminar los saltos de línea y los espacios extras
                linea = linea.strip().rstrip(';')
                
                if not linea:  # Si la línea está vacía, la ignoramos
                    continue
                
                # Separar los campos por coma y espacio (formato: campo1, campo2, ...)
                campos = [campo.strip() for campo in linea.split(':')]
                
                if len(campos) != 4:
                    messagebox.showerror("Error", f"Formato incorrecto en la línea: {linea}")
                    continue
                
                placa, marca, modelo, precio = campos
                
                # Validación de los datos
                try:
                    precio = float(precio)
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un número decimal.")
                    continue
                
                # Crear un nuevo vehiculo y agregarlo a la lista circular
                nuevo_vehiculo = vehiculo(placa, marca, modelo, precio)
                vehiculos.insertar_valor(nuevo_vehiculo)
                
            messagebox.showinfo("Carga Masiva", "Vehiculos cargados exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al cargar los vehiculos: {e}")

def carga_masiva_vehiculos():
    archivo = askopenfilename(title="Seleccionar archivo de texto", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        cargar_vehiculos_desde_texto(archivo)

def cargar_rutas_desde_texto(ruta_archivo):
    try:
        with open(ruta_archivo, mode='r') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                # Eliminar los saltos de línea y los espacios extras
                linea = linea.strip().rstrip('%')
                
                if not linea:  # Si la línea está vacía, la ignoramos
                    continue
                
                # Separar los campos por coma y espacio (formato: campo1, campo2, ...)
                campos = [campo.strip() for campo in linea.split('/')]
                
                if len(campos) != 3:
                    messagebox.showerror("Error", f"Formato incorrecto en la línea: {linea}")
                    continue
                
                origen, destino, tiempo_ruta = campos
                
                # Crear un nuevo vehiculo y agregarlo a la lista circular
                nueva_ruta = ruta(origen, destino, tiempo_ruta)
                destinos.insertar(nueva_ruta)
                
            messagebox.showinfo("Carga Masiva", "Vehiculos cargados exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al cargar los vehiculos: {e}")
    
def carga_masiva_rutas():
    archivo = askopenfilename(title="Seleccionar archivo de texto", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        cargar_rutas_desde_texto(archivo)

def load_routes():
    messagebox.showinfo("Cargar Rutas", "Cargando archivo de rutas y generando el grafo...")

def mass_upload_clients():
    messagebox.showinfo("Carga Masiva", "Carga masiva de clientes realizada.")

def mass_upload_vehicles():
    messagebox.showinfo("Carga Masiva", "Carga masiva de vehículos realizada.")
    
def create_item(entity):
    messagebox.showinfo(f"Crear {entity}", f"Crear {entity} ingresando datos.")

def modify_item(entity):
    messagebox.showinfo(f"Modificar {entity}", f"Modificar {entity} ingresando llave.")

def delete_item(entity):
    messagebox.showinfo(f"Eliminar {entity}", f"Eliminar {entity} ingresando llave.")

def show_info(entity):
    messagebox.showinfo(f"Mostrar Información {entity}", f"Mostrar información de {entity} ingresando llave.")

def show_data_structure(entity):
    messagebox.showinfo(f"Mostrar Estructura de Datos {entity}", f"Mostrar estructura de datos ({entity}) en Graphviz.")

def generate_reports():
    messagebox.showinfo("Generar Reportes", "Generando reportes...")
    
def ventana_crear_cliente():
    ventana_cliente = tk.Toplevel()
    ventana_cliente.title("Crear Cliente")
    ventana_cliente.geometry("400x500")
    
    # Etiquetas y campos de entrada
    tk.Label(ventana_cliente, text="DPI:").pack(pady=5)
    dpi_entry = tk.Entry(ventana_cliente)
    dpi_entry.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Nombres:").pack(pady=5)
    nombres_entry = tk.Entry(ventana_cliente)
    nombres_entry.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Apellidos:").pack(pady=5)
    apellidos_entry = tk.Entry(ventana_cliente)
    apellidos_entry.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Genero:").pack(pady=5)
    genero_combobox = ttk.Combobox(ventana_cliente, values=["F", "M"], state="readonly")
    genero_combobox.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Teléfono:").pack(pady=5)
    telefono_entry = tk.Entry(ventana_cliente)
    telefono_entry.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Dirección:").pack(pady=5)
    direccion_entry = tk.Entry(ventana_cliente)
    direccion_entry.pack(pady=5)
    
    def submit_data():
        """Recoger datos y cerrar la ventana emergente."""
        
        dpi = dpi_entry.get()
        nombres = nombres_entry.get()
        apellidos = apellidos_entry.get()
        genero = genero_combobox.get()
        telefono = telefono_entry.get()
        direccion = direccion_entry.get()
        
        # Validación de teléfono (debe ser numérico)
        if not dpi.isdigit():
            messagebox.showerror("Error", "El dpi debe ser un número.")
            return
        
        # Validación de DPI (debe ser numérico)
        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe ser un número.")
            return
        
        # Crear cliente
        nuevo_cliente = cliente(dpi, nombres, apellidos, genero, telefono, direccion)
        clientes.insertar(nuevo_cliente)
        
        
        
        messagebox.showinfo("Datos del Cliente", f"Cliente creado:\nDPI: {dpi}\nNombres: {nombres}\nApellidos: {apellidos}\nGenero: {genero}\nTeléfono: {telefono}\nDirección: {direccion}")
        ventana_cliente.destroy()

    submit_button = tk.Button(ventana_cliente, text="Crear Cliente", command=submit_data)
    submit_button.pack(pady=20)
    
def ventana_modificar_cliente():
    ventana_cliente = tk.Toplevel()
    ventana_cliente.title("Modificar Cliente")
    ventana_cliente.geometry("400x300")
    
    # Etiquetas y campos de entrada
    tk.Label(ventana_cliente, text="DPI:").pack(pady=5)
    dpi_entry = tk.Entry(ventana_cliente)
    dpi_entry.pack(pady=5)
    
    def submit_data():
        """Verificar que exista el cliente a modificar"""
        
        dpi = dpi_entry.get()
        
        # Validación de DPI (debe ser numérico)
        if not dpi.isdigit():
            messagebox.showerror("Error", "El dpi debe ser un número")
            return
        
        # Buscar cliente
        nodo_a_modificar = clientes.buscar(int(dpi))
        
        # Validar que exista el cliente a modificar
        if nodo_a_modificar is None:
            messagebox.showerror("Error", "El cliente no existe.")
            return
        
        # Mostrar datos del cliente encontrados (opcional)
        messagebox.showinfo("Éxito", f"Cliente encontrado {nodo_a_modificar.getCliente().getNombres()}")
       
        
        ventana_nuevos_datos_cliente(nodo_a_modificar)
        
        ventana_cliente.destroy()
    
    submit_button = tk.Button(ventana_cliente, text="Modificar Cliente", command=submit_data)
    submit_button.pack(pady=20)

def ventana_nuevos_datos_cliente(nodo):
    ventana_cliente = tk.Toplevel()
    ventana_cliente.title(f"Nuevos datos cliente: {nodo.getCliente().getDpi()}")
    ventana_cliente.geometry("400x500")
    
    tk.Label(ventana_cliente, text="Nombres:").pack(pady=5)
    nombres_entry = tk.Entry(ventana_cliente)
    nombres_entry.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Apellidos:").pack(pady=5)
    apellidos_entry = tk.Entry(ventana_cliente)
    apellidos_entry.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Genero:").pack(pady=5)
    genero_combobox = ttk.Combobox(ventana_cliente, values=["F", "M"], state="readonly")
    genero_combobox.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Teléfono:").pack(pady=5)
    telefono_entry = tk.Entry(ventana_cliente)
    telefono_entry.pack(pady=5)
    
    tk.Label(ventana_cliente, text="Dirección:").pack(pady=5)
    direccion_entry = tk.Entry(ventana_cliente)
    direccion_entry.pack(pady=5)
    
    # Precargar los campos con datos del cliente
    nombres_entry.insert(0, nodo.getCliente().getNombres())  # Precargar nombres
    apellidos_entry.insert(0, nodo.getCliente().getApellidos())  # Precargar apellidos
    genero_combobox.set(nodo.getCliente().getGenero())  # Precargar género
    telefono_entry.insert(0, str(nodo.getCliente().getTelefono()))  # Precargar teléfono
    direccion_entry.insert(0, nodo.getCliente().getDireccion())  # Precargar dirección
    
    def submit_data():
        """Recoger datos y cerrar la ventana emergente."""
        
        nombres = nombres_entry.get()
        apellidos = apellidos_entry.get()
        genero = genero_combobox.get()
        telefono = telefono_entry.get()
        direccion = direccion_entry.get()
        
        # Validación de teléfono (debe ser numérico)
        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe ser un número.")
            return
        
        # Modificar cliente
        nodo.getCliente().setNombres(nombres)
        nodo.getCliente().setApellidos(apellidos)
        nodo.getCliente().setGenero(genero)
        nodo.getCliente().setTelefono(telefono)
        nodo.getCliente().setDireccion(direccion)
        
        messagebox.showinfo("Datos del Cliente", f"Datos modificados:\nDPI: {nodo.getCliente().getDpi()}\nNombres: {nodo.getCliente().getNombres()}\nApellidos: {nodo.getCliente().getApellidos()}\nGenero: {nodo.getCliente().getGenero()}\nTeléfono: {nodo.getCliente().getTelefono()}\nDirección: {nodo.getCliente().getDireccion()}")
        ventana_cliente.destroy()

    submit_button = tk.Button(ventana_cliente, text="Modificar Cliente", command=submit_data)
    submit_button.pack(pady=20)
    
def ventana_eliminar_cliente():
    ventana_cliente = tk.Toplevel()
    ventana_cliente.title("Eliminar Cliente")
    ventana_cliente.geometry("400x300")
    
    # Etiquetas y campos de entrada
    tk.Label(ventana_cliente, text="DPI:").pack(pady=5)
    dpi_entry = tk.Entry(ventana_cliente)
    dpi_entry.pack(pady=5)
    
    def submit_data():
        """Verificar que exista el cliente a modificar"""
        
        dpi = dpi_entry.get()
        
        # Validación de DPI (debe ser numérico)
        if not dpi.isdigit():
            messagebox.showerror("Error", "El dpi debe ser un número")
            return
        
        # Buscar cliente
        nodo_a_eliminar = clientes.buscar(int(dpi))
        
        # Validar que exista el cliente a modificar
        if nodo_a_eliminar is None:
            messagebox.showerror("Error", "El cliente no existe.")
            return
        
        nombre = nodo_a_eliminar.getCliente().getNombres()
        
        # Eliminar cliente
        clientes.eliminar(int(dpi))
        
        # Mostrar datos del cliente encontrados (opcional)
        messagebox.showinfo("Éxito", f"Cliente {nombre} eliminado...")
        
        ventana_cliente.destroy()
    
    submit_button = tk.Button(ventana_cliente, text="Eliminar Cliente", command=submit_data)
    submit_button.pack(pady=20)
    
def ventana_mostrar_cliente():
    ventana_cliente = tk.Toplevel()
    ventana_cliente.title("Mostrar información de Cliente")
    ventana_cliente.geometry("400x300")
    
    # Etiquetas y campos de entrada
    tk.Label(ventana_cliente, text="DPI:").pack(pady=5)
    dpi_entry = tk.Entry(ventana_cliente)
    dpi_entry.pack(pady=5)
    
    def submit_data():
        """Verificar que exista el cliente a mostrar"""
        
        dpi = dpi_entry.get()
        
        # Validación de DPI (debe ser numérico)
        if not dpi.isdigit():
            messagebox.showerror("Error", "El dpi debe ser un número")
            return
        
        # Buscar cliente
        nodo_a_buscar = clientes.buscar(int(dpi))
        
        # Validar que exista el cliente a modificar
        if nodo_a_buscar is None:
            messagebox.showerror("Error", "El cliente no existe.")
            return
        
        info_cliente = f"Nombre: {nodo_a_buscar.getCliente().getNombres()}\nApellidos: {nodo_a_buscar.getCliente().getApellidos()}\nGénero: {nodo_a_buscar.getCliente().getGenero()}\nTeléfono: {nodo_a_buscar.getCliente().getTelefono()}\nDirección: {nodo_a_buscar.getCliente().getDireccion()}"
        
        # Mostrar datos del cliente encontrados
        info_label.config(text= f"INFORMACIÓN DEL CLIENTE\n\n{info_cliente}")
        info_label.pack()
        info_label.place(x=50, y=250, width=500, height=500)
        
        ventana_cliente.destroy()
    
    submit_button = tk.Button(ventana_cliente, text="Mostrar información", command=submit_data)
    submit_button.pack(pady=20)
    
def ventana_crear_vehiculo():
    ventana_vehiculo = tk.Toplevel()
    ventana_vehiculo.title("Crear Vehiculo")
    ventana_vehiculo.geometry("400x500")
    
    # Etiquetas y campos de entrada
    tk.Label(ventana_vehiculo, text="Placa:").pack(pady=5)
    placa_entry = tk.Entry(ventana_vehiculo)
    placa_entry.pack(pady=5)
    
    tk.Label(ventana_vehiculo, text="Marca:").pack(pady=5)
    marca_entry = tk.Entry(ventana_vehiculo)
    marca_entry.pack(pady=5)
    
    tk.Label(ventana_vehiculo, text="Modelo:").pack(pady=5)
    modelo_entry = tk.Entry(ventana_vehiculo)
    modelo_entry.pack(pady=5)
    
    tk.Label(ventana_vehiculo, text="Precio por segundo (Q):").pack(pady=5)
    precio_entry = tk.Entry(ventana_vehiculo)
    precio_entry.pack(pady=5)
    
    def submit_data():
        """Recoger datos y cerrar la ventana emergente."""
        
        placa = placa_entry.get()
        marca = marca_entry.get()
        modelo = modelo_entry.get()
        precio = precio_entry.get()
        
        # Validación de precio (debe ser decimal)
        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número decimal.")
            return
        
        # Crear vehículo
        nuevo_vehiculo = vehiculo(placa, marca, modelo, precio)
        vehiculos.insertar_valor(nuevo_vehiculo)
        
        messagebox.showinfo("Datos del Vehículo", f"Vehículo creado:\nPlaca: {placa}\nMarca: {marca}\nModelo: {modelo}\nPrecio por segundo: Q{precio}")
        ventana_vehiculo.destroy()

    submit_button = tk.Button(ventana_vehiculo, text="Crear Vehiculo", command=submit_data)
    submit_button.pack(pady=20)
    
def ventana_modificar_vehiculo():
    ventana_vehiculo = tk.Toplevel()
    ventana_vehiculo.title("Modificar Vehículo")
    ventana_vehiculo.geometry("400x300")
    
    # Etiquetas y campos de entrada
    tk.Label(ventana_vehiculo, text="Placa:").pack(pady=5)
    placa_entry = tk.Entry(ventana_vehiculo)
    placa_entry.pack(pady=5)
    
    def submit_data():
        """Verificar que exista el vehiculo a modificar"""
        
        placa = placa_entry.get()
        
        # Buscar vehiculo
        vehiculo_a_modificar = vehiculos.buscar_vehiculo(placa)
        
        # Validar que exista el vehiculo a modificar
        if vehiculo_a_modificar is None:
            messagebox.showerror("Error", "El vehiculo no existe.")
            return
        
        # Mostrar datos del vehículo encontrado (opcional)
        messagebox.showinfo("Éxito", f"Vehículo encontrado {vehiculo_a_modificar.getPlaca()}")
        
        ventana_nuevos_datos_vehiculo(vehiculo_a_modificar)
        
        ventana_vehiculo.destroy()
    
    submit_button = tk.Button(ventana_vehiculo, text="Modificar Vehículo", command=submit_data)
    submit_button.pack(pady=20)
    
def ventana_nuevos_datos_vehiculo(vehiculo: vehiculo):
    ventana_vehiculo = tk.Toplevel()
    ventana_vehiculo.title("Modificar Vehículo")
    ventana_vehiculo.geometry("400x500")
    
    # Etiquetas y campos de entrada
    
    tk.Label(ventana_vehiculo, text="Precio por segundo (Q):").pack(pady=5)
    precio_entry = tk.Entry(ventana_vehiculo)
    precio_entry.pack(pady=5)
    
    precio_entry.insert(0, vehiculo.getPrecioSegundo())
    
    def submit_data():
        """Recoger datos y cerrar la ventana emergente."""
        precio = precio_entry.get()
        
        # Validación de precio (debe ser decimal)
        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número decimal.")
            return
        
        # Modificar vehículo
        vehiculo.setPrecioSegundo(precio)
        
        messagebox.showinfo("Datos del Vehículo", f"Vehículo modificado:\nPlaca: {vehiculo.getPlaca()}\nMarca: {vehiculo.getMarca()}\nModelo: {vehiculo.getModelo()}\nPrecio por segundo: Q{vehiculo.getPrecioSegundo()}")
        
        ventana_vehiculo.destroy()

    submit_button = tk.Button(ventana_vehiculo, text="Modificar Vehiculo", command=submit_data)
    submit_button.pack(pady=20)

def ventana_eliminar_vehiculo():
    messagebox.showinfo("Fracaso", "No se pudo eliminar el vehículo.")
    
def ventana_mostrar_vehiculo():
    ventana_vehiculo = tk.Toplevel()
    ventana_vehiculo.title("Mostrar datos de vehículo")
    ventana_vehiculo.geometry("400x300")
    
    # Etiquetas y campos de entrada
    tk.Label(ventana_vehiculo, text="Placa:").pack(pady=5)
    placa_entry = tk.Entry(ventana_vehiculo)
    placa_entry.pack(pady=5)
    
    def submit_data():
        """Verificar que exista el vehiculo a mostrar"""
        
        placa = placa_entry.get()
        
        # Buscar vehiculo
        vehiculo_a_mostrar:vehiculo = vehiculos.buscar_vehiculo(placa)
        
        # Validar que exista el vehiculo a modificar
        if vehiculo_a_mostrar is None:
            messagebox.showerror("Error", "El vehiculo no existe.")
            return
        
        info_vehiculo = f"Placa: {vehiculo_a_mostrar.getPlaca()}\nMarca: {vehiculo_a_mostrar.getMarca()}\nModelo: {vehiculo_a_mostrar.getModelo()}\nPrecio por segundo: Q{vehiculo_a_mostrar.getPrecioSegundo()}"
        
        # Mostrar datos del cliente encontrados
        info_label.config(text= f"INFORMACIÓN DEL VEHÍCULO\n\n{info_vehiculo}")
        info_label.pack()
        info_label.place(x=50, y=250, width=500, height=500)
        
        ventana_vehiculo.destroy()
    
    submit_button = tk.Button(ventana_vehiculo, text="Mostrar datos de Vehículo", command=submit_data)
    submit_button.pack(pady=20)
    
def mostrar_estructura(entity):
    if entity == "clientes":
        clientes.mostrarEstructura()
    elif entity == "vehiculos":
        vehiculos.mostrar_estructura()
    
    #verificar si existe la imagen
    imagen_estructura_original = Image.open("src/images/estructura.png")
    imagen_estructura_ajustada = imagen_estructura_original.resize((800, 400), Image.Resampling.LANCZOS)
    imagen_estructura = ImageTk.PhotoImage(imagen_estructura_ajustada)
    imagen_estructura_label.config(image=imagen_estructura)
    imagen_estructura_label.image = imagen_estructura
    imagen_estructura_label.place(x=600, y=50, width=700, height=400)

        
# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Rutas, Clientes, Vehículos y Viajes")
root.geometry("1450x850")

# Imagen de fondo
fondo = tk.PhotoImage(file = "src/images/fondo.png")
fondo_label = tk.Label(root, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Usamos place para que ocupe toda la ventana

# Imagen estructura
imagen_estructura_original = Image.open("src/images/estructura.png")
imagen_estructura_ajustada = imagen_estructura_original.resize((800, 400), Image.Resampling.LANCZOS)
imagen_estructura = ImageTk.PhotoImage(imagen_estructura_ajustada)
imagen_estructura_label = tk.Label(root, image=imagen_estructura)
imagen_estructura_label.image = imagen_estructura
imagen_estructura_label.place_forget()

#Ventana dinámica
info_label = tk.Label(root, text="Hola", font=("Arial", 18), bg="#013c6c", fg="white", anchor="w", justify="left")
info_label.place(x=50, y=250, width=500, height=500)
info_label.place_forget()

#Botón para salir de la aplicación
tk.Button(root, text="Salir", command=root.quit, bg="#FF5733", fg="white", font=("Arial", 12), relief="raised").place(x=800, y=750, width=120, height=40)

#Botón para limpiar la pantalla
tk.Button(root, text="Limpiar Pantalla", command=lambda: reiniciar(), bg="#FF5733", fg="white", font=("Arial", 12), relief="raised").place(x=700, y=750, width=120, height=40)

# Pie de página
footer_frame = Frame(root, bg="#000569", height=40)
footer_frame.pack(side="bottom", fill="x")
footer_label = Label(footer_frame, text="Desarrollado por Nelson Emanuel Cún Bálan", font=("Arial", 12), fg="white", bg="#000569")
footer_label.pack()

# Menú principal
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Menú de Rutas
routes_menu = Menu(menu_bar, tearoff=0)
routes_menu.add_command(label="Cargar Archivo de Rutas", command=load_routes)
menu_bar.add_cascade(label="Rutas", menu=routes_menu)

# Menú de Clientes
clients_menu = Menu(menu_bar, tearoff=0)
clients_menu.add_command(label="Crear Cliente", command=lambda: ventana_crear_cliente())
clients_menu.add_command(label="Modificar Cliente", command=lambda: ventana_modificar_cliente())
clients_menu.add_command(label="Eliminar Cliente", command=lambda: ventana_eliminar_cliente())
clients_menu.add_command(label="Mostrar Información de Cliente", command=lambda: ventana_mostrar_cliente())
clients_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: mostrar_estructura("clientes"))
clients_menu.add_command(label="Carga Masiva de Clientes", command=lambda: carga_masiva_clientes())
menu_bar.add_cascade(label="Clientes", menu=clients_menu)

# Menú de Vehículos
vehicles_menu = Menu(menu_bar, tearoff=0)
vehicles_menu.add_command(label="Crear Vehículo", command=lambda: ventana_crear_vehiculo())
vehicles_menu.add_command(label="Modificar Vehículo", command=lambda: ventana_modificar_vehiculo())
vehicles_menu.add_command(label="Eliminar Vehículo", command=lambda: ventana_eliminar_vehiculo())
vehicles_menu.add_command(label="Mostrar Información de Vehículo", command=lambda: ventana_mostrar_vehiculo())
vehicles_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: mostrar_estructura("vehiculos"))
vehicles_menu.add_command(label="Carga Masiva de Vehículos", command=lambda: carga_masiva_vehiculos())
menu_bar.add_cascade(label="Vehículos", menu=vehicles_menu)

# Menú de Viajes
trips_menu = Menu(menu_bar, tearoff=0)
trips_menu.add_command(label="Crear Viaje", command=lambda: create_item("Viaje"))
trips_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: show_data_structure("Viajes"))
menu_bar.add_cascade(label="Viajes", menu=trips_menu)

# Menú de Reportes
reports_menu = Menu(menu_bar, tearoff=0)
reports_menu.add_command(label="Generar Reportes", command=generate_reports)
menu_bar.add_cascade(label="Reportes", menu=reports_menu)

# Iniciar la aplicación
root.mainloop()
