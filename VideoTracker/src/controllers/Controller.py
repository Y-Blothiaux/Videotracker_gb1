
from models.fileRepo import FileRepo
from models.point import Point
from random import randint
import PIL.Image,PIL.ImageTk


class Controller:

    def __init__(self, video, view, point, filerepo, graph):
        
        self.Video = video
        self.view = view
        self.Point = point
        self.FileRepo = filerepo
        self.Graph = graph
        self.view.Fichier.entryconfig(0, command=self.LoadVideo) # 0 = Fichier.index("Import Vidéo")
        self.view.Fichier.entryconfig(1, command=self.Pause)
        self.view.Fichier.entryconfig(2, command=lambda: self.ExportCSV(self.pointageData()))
        self.view.Fichier.entryconfig(4, command=self.Quit)
        
        self.view.menu_graph.entryconfig(0, command=self.graph_xy)
        self.view.menu_graph.entryconfig(1, command=self.graph_xt)
        self.view.menu_graph.entryconfig(2, command=self.graph_yt)

        self.view.menu_edit.entryconfig(0, command= self.display_positions)

        self.view.FramePauseButton.configure(command=self.Pause)
        self.view.FirstFrameButton.configure(command=self.debut_video)
        self.view.NextFrameButton.configure(command=self.next_frame)
        self.view.PreviousFrameButton.configure(command=self.previous_frame)
        self.view.LastFrameButton.configure(command=self.fin_video)
    
        
            
    def LoadVideo(self):
        self.Video.open_file()
        self.Video.play_video()

    def Quit(self):
        print("Quitting")
        self.Video.window.destroy()

    def Pause(self):
        
        if self.Video.pause:
            print("Playing Video")
            self.view.FramePauseButton.configure(text="⏸️")
            self.Video.pause=False
            self.Video.play_video()
        else:
            print("Paused")
            self.view.FramePauseButton.configure(text="▶")
            self.Video.pause=True

    def debut_video(self):
        print('First frame...')
        self.view.FramePauseButton.configure(text="▶")
        self.Video.first_frame()

    def fin_video(self):
        print('Last frame...')
        self.view.FramePauseButton.configure(text="▶")
        self.Video.last_frame()
    
    def next_frame(self):
        print('Next frame...')
        self.view.FramePauseButton.configure(text="▶")
        self.Video.image_forward()
    
    def previous_frame(self):
        print('Previous frame...')
        self.view.FramePauseButton.configure(text="▶")
        self.Video.image_backward()
    
    def randomData(self,n):
        #permet de construire une liste avec n points qui ont des coordonnées aléatoires.
        lPoints = []
        for i in range(n):
            rdPoint = Point(randint(-200,200),randint(-200,200))
            lPoints.append((rdPoint.getx(),rdPoint.gety()))
        return lPoints
    
    def pointageData(self):
        click_positions = self.Video.click_positions
        return click_positions
    
    def ExportCSV(self,data):
        contenuDuCSV = FileRepo.dataToCSV(data)
        self.FileRepo.saveFile("CSVtest.csv",contenuDuCSV)
    
    def graph_xy(self):
        self.Graph.new_graph_xy()
    
    def graph_xt(self):
        self.Graph.new_graph_xt()

    def graph_yt(self):
        self.Graph.new_graph_yt()

    def display_positions(self):
        self.Video.display_values_xy()