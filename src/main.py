import tkinter as tk
from gui.clientes import abrir_clientes
from database.init_db import createDB
# from peliculas import abrir_peliculas
# from copias import abrir_copias

def main_menu():
    createDB()
    root = tk.Tk()
    root.title("Sistema de Gestión de Películas")

    # Botón para abrir interfaz de clientes
    btn_clientes = tk.Button(root, text="Gestionar Clientes", command=abrir_clientes)
    btn_clientes.pack(pady=10)

    # Botón para abrir interfaz de películas
    btn_peliculas = tk.Button(root, text="Gestionar Películas")
    btn_peliculas.pack(pady=10)

    # Botón para abrir interfaz de cintas
    btn_cintas = tk.Button(root, text="Gestionar Cintas")
    btn_cintas.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_menu()