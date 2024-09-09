from tkinter import *
import tkinter as tk
from database.init_db import createDB
from gui.clientes import client
from gui.peliculas import pelicula
from gui.copias import copia

class main_menu:

    def __init__(self, window_menu):

        self.wmenu = window_menu;
        self.wmenu.title("Menu principal")

        # Creacion del frame principal
        frame = LabelFrame(self.wmenu, text= "Base de datos")
        frame.grid(row = 0, column=0, columnspan= 3, pady= 20)

        # Creacion de botones
        self.bclient =  tk.Button(frame, text= "Clientes").grid(row=1, column=0)
        self.bcopias =  tk.Button(frame, text= "Copias").grid(row=1, column=1)
        self.bpeliculas =  tk.Button(frame, text= "Peliculas").grid(row=1, column=2)

        pass
    

if __name__ == "__main__":
    createDB()
    root = tk.Tk() # Ventana principal
    # Ventaas para administrar la db
    vclientes = tk.Toplevel(root)
    vcopias = tk.Toplevel(root)
    vpeliculas = tk.Toplevel(root)
    # Proyeccion en su objeto
    menu = main_menu(root)
    clients = client(vclientes)
    copias = copia(vcopias)
    peliculas = pelicula(vpeliculas)
    root.mainloop()