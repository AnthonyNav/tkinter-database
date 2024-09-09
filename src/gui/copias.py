from tkinter import *
import tkinter as tk

class copia:
    def __init__(self, window_client):

        self.wclient = window_client;
        self.wclient.title("Administrar Clientes")

        # Creacion del frame principal
        frame = LabelFrame(self.wclient, text= "Administrador de clentes")
        frame.grid(row = 0, column=0, columnspan= 3, pady= 20)

        pass