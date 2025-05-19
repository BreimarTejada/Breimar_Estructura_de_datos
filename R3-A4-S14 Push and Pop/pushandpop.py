import tkinter as tk
from tkinter import messagebox
from collections import deque

# Crear la bicola
bicola = deque()

# Funciones
def insertar_derecha():
    valor = entrada.get()
    if valor:
        bicola.append(valor)
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un valor.")

def insertar_izquierda():
    valor = entrada.get()
    if valor:
        bicola.appendleft(valor)
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un valor.")

def atender_derecha():
    if bicola:
        eliminado = bicola.pop()
        actualizar_lista()
        messagebox.showinfo("Atendido por la derecha", f"Se eliminó: {eliminado}")
    else:
        messagebox.showwarning("Advertencia", "La bicola está vacía.")

def atender_izquierda():
    if bicola:
        eliminado = bicola.popleft()
        actualizar_lista()
        messagebox.showinfo("Atendido por la izquierda", f"Se eliminó: {eliminado}")
    else:
        messagebox.showwarning("Advertencia", "La bicola está vacía.")

def actualizar_lista():
    if bicola:
        contenido = " ← ".join(bicola)
        etiqueta_lista.config(text=f" {contenido}")
    else:
        etiqueta_lista.config(text="Bicola vacía")

# Ventana principal
ventana = tk.Tk()
ventana.title("Bicola - Interfaz Gráfica")
ventana.geometry("500x300")
ventana.resizable(False, False)

# Entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Botones de inserción
frame_insertar = tk.Frame(ventana)
frame_insertar.pack(pady=5)

tk.Button(frame_insertar, text="Insertar por la izquierda", command=insertar_izquierda, bg="#aed6f1").pack(side=tk.LEFT, padx=5)
tk.Button(frame_insertar, text="Insertar por la derecha", command=insertar_derecha, bg="#a9dfbf").pack(side=tk.LEFT, padx=5)

# Botones de atención
frame_atender = tk.Frame(ventana)
frame_atender.pack(pady=5)

tk.Button(frame_atender, text="Atender por la izquierda", command=atender_izquierda, bg="#f9e79f").pack(side=tk.LEFT, padx=5)
tk.Button(frame_atender, text="Atender por la derecha", command=atender_derecha, bg="#f5b7b1").pack(side=tk.LEFT, padx=5)

# Etiqueta para mostrar elementos de la bicola
etiqueta_lista = tk.Label(ventana, text="Bicola vacía", font=("Arial", 12), wraplength=480, justify="center")
etiqueta_lista.pack(pady=20)

# Ejecutar ventana
ventana.mainloop()
