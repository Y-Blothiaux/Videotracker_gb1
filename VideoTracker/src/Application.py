from models.Video import Video
from views.view import View
from models.Graph import Graphique
from models.fileRepo import FileRepo
from models.point import Point
import pandas as pd
from matplotlib import pyplot as plt
from controllers.Controller import Controller
import tkinter as tk

class Application(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title('Video Tracker')
        
        # create a video model
        video = Video(self,self.title)

        # create a view and place it on the root window
        view = View(self)

        point = Point(x=0,y=0)

        filerepo = FileRepo(filename='',fileContent='')

        graph = Graphique(filename='',fileContent='')

        # create a controller
        controller = Controller(video, view, point, filerepo, graph)

        # set the controller to view
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()