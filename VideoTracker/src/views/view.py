from controllers.Controller import Controller
from models.Video import Video

import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import *

class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


        #Création menu déroulant 'Fichier'
    
        mon_menu = tk.Menu(self.parent)
        self.parent.config(menu=mon_menu)

        Fichier = tk.Menu(mon_menu, tearoff=0)
        self.Fichier = Fichier # LA LIGNE QUI MANQUAIT
        Fichier.add_command(label='Charger un fichier vidéo')
        Fichier.add_command(label='Lire une vidéo')
        Fichier.add_command(label='Export CSV')

        # Un menu déroulant dans le menu File.
        menu_graph = tk.Menu(mon_menu, tearoff=0)
        self.menu_graph = menu_graph
        menu_graph.add_command(label="y(x)")
        menu_graph.add_command(label="x(t)")
        menu_graph.add_command(label="y(t)")
        Fichier.add_cascade(label="View", menu=menu_graph)  

        Fichier.add_command(label='Quitter')       
        mon_menu.add_cascade(label='Fichier', menu=Fichier)


        menu_edit = tk.Menu(mon_menu, tearoff=0)
        self.menu_edit = menu_edit
        menu_edit.add_command(label="Valeurs X, Y")
        mon_menu.add_cascade(label="Edit", menu=menu_edit)


        #Boutons lecteur vidéo

        self.frame = tk.LabelFrame(self.parent)
        self.FirstFrameButton = tk.Button(self.frame,text = "⏮")
        self.FirstFrameButton.pack(side = LEFT)
        self.PreviousFrameButton = tk.Button(self.frame,text = "⏪")
        self.PreviousFrameButton.pack(side = LEFT)
        self.FramePauseButton = tk.Button(self.frame,text="▶️")
        self.FramePauseButton.pack(side = LEFT)
        self.NextFrameButton = tk.Button(self.frame,text = "⏩")
        self.NextFrameButton.pack(side = LEFT)
        self.LastFrameButton = tk.Button(self.frame,text = "⏭")
        self.LastFrameButton.pack(side = LEFT)
        self.frame.pack(side=BOTTOM, pady=50)
        self.canvas = tk.Canvas(self.parent)
        self.canvas.pack()
        self.pause = False
        

    
        

    def setController(self, controller):
        self.controller = controller

