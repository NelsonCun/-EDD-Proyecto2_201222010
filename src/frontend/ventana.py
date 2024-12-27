from src.structs.listaCircular.listaCircular import listaCircular
from src.classes.cliente import cliente
import tkinter as tk
from tkinter import Menu, messagebox, Frame, Label, Button, ttk

clientes = listaCircular()

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
    ventana_cliente.geometry("400x500")


# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Rutas, Clientes, Vehículos y Viajes")
root.geometry("1450x850")

# Imagen de fondo
fondo = tk.PhotoImage(file = "src/images/fondo.png")
fondo_label = tk.Label(root, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Usamos place para que ocupe toda la ventana

# Usar un botón estándar de tkinter, no un ttk
tk.Button(root, text="Salir", command=root.quit, bg="#FF5733", fg="white", font=("Arial", 12), relief="raised").place(x=800, y=750, width=120, height=40)

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
clients_menu.add_command(label="Eliminar Cliente", command=lambda: modify_item("Cliente"))
clients_menu.add_command(label="Mostrar Información de Cliente", command=lambda: show_info("Cliente"))
clients_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: show_data_structure("Clientes"))
clients_menu.add_command(label="Carga Masiva de Clientes", command=mass_upload_clients)
menu_bar.add_cascade(label="Clientes", menu=clients_menu)

# Menú de Vehículos
vehicles_menu = Menu(menu_bar, tearoff=0)
vehicles_menu.add_command(label="Crear Vehículo", command=lambda: create_item("Vehículo"))
vehicles_menu.add_command(label="Modificar Vehículo", command=lambda: modify_item("Vehículo"))
vehicles_menu.add_command(label="Eliminar Vehículo", command=lambda: delete_item("Vehículo"))
vehicles_menu.add_command(label="Mostrar Información de Vehículo", command=lambda: show_info("Vehículo"))
vehicles_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: show_data_structure("Vehículos"))
vehicles_menu.add_command(label="Carga Masiva de Vehículos", command=mass_upload_vehicles)
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
