import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.inicio = None

    def insertar_cliente(self, cedula, nombre):
        nuevo_nodo = Nodo(cedula, nombre)
        if not self.inicio:
            self.inicio = nuevo_nodo
            self.inicio.siguiente = self.inicio
        else:
            temp = self.inicio
            while temp.siguiente != self.inicio:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.inicio

    def listar_clientes(self):
        clientes = []
        if not self.inicio:
            return ["La lista está vacía."]
        temp = self.inicio
        while True:
            clientes.append(f"Cédula: {temp.cedula}, Nombre: {temp.nombre}")
            temp = temp.siguiente
            if temp == self.inicio:
                break
        return clientes

class Aplicacion:
    def __init__(self, root):
        self.lista = ListaCircular()
        self.root = root
        self.root.title("Gestión de Clientes")
        self.root.configure(bg="#E8F0F2")  # Color de fondo
        
        # Configuración de fuente y estilos
        font_label = ("Arial", 12, "bold")
        font_button = ("Arial", 12)
        
        tk.Label(root, text="Cédula:", font=font_label, bg="#E8F0F2").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.cedula_entry = tk.Entry(root, font=font_label)
        self.cedula_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nombre:", font=font_label, bg="#E8F0F2").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.nombre_entry = tk.Entry(root, font=font_label)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón de Insertar Cliente
        self.insertar_btn = tk.Button(root, text="Insertar Cliente", font=font_button, bg="#4CAF50", fg="white", command=self.insertar_cliente)
        self.insertar_btn.grid(row=2, column=0, columnspan=2, pady=5)

        # Botón de Listar Clientes
        self.listar_btn = tk.Button(root, text="Listar Clientes", font=font_button, bg="#2196F3", fg="white", command=self.listar_clientes)
        self.listar_btn.grid(row=3, column=0, columnspan=2, pady=5)

        # Botón para Salir
        self.salir_btn = tk.Button(root, text="Salir", font=font_button, bg="#F44336", fg="white", command=root.quit)
        self.salir_btn.grid(row=4, column=0, columnspan=2, pady=5)

    def insertar_cliente(self):
        cedula = self.cedula_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        if cedula and nombre:
            self.lista.insertar_cliente(cedula, nombre)
            messagebox.showinfo("Éxito", "Cliente insertado correctamente.")
            self.cedula_entry.delete(0, tk.END)
            self.nombre_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Debe ingresar cédula y nombre.")

    def listar_clientes(self):
        clientes = self.lista.listar_clientes()
        messagebox.showinfo("Lista de Clientes", "\n".join(clientes))

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()