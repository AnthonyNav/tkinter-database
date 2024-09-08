import tkinter as tk
import sqlite3

def abrir_clientes():
    window = tk.Toplevel()
    window.title("Gestionar Clientes")

    # Crear un formulario para agregar un nuevo cliente
    tk.Label(window, text="Nombre:").pack()
    nombre_entry = tk.Entry(window)
    nombre_entry.pack()

    tk.Label(window, text="Dirección:").pack()
    direccion_entry = tk.Entry(window)
    direccion_entry.pack()

    def agregar_cliente():
        nombre = nombre_entry.get()
        direccion = direccion_entry.get()
        conn = sqlite3.connect('src/database/movies.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Clientes (nombre, direccion) VALUES (?, ?)", (nombre, direccion))
        conn.commit()
        conn.close()

    btn_agregar = tk.Button(window, text="Agregar Cliente", command=agregar_cliente)
    btn_agregar.pack()

    window.mainloop()
