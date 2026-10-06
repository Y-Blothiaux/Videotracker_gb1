from tkinter import filedialog
import pandas as pd
from matplotlib import pyplot as plt
import csv

class Graphique:
    def __init__(self,filename,fileContent):
        self.__filename = filename
        self.__fileContent = fileContent
    
    def new_graph_xy(self):
        x = []
        y = []

        with open(filedialog.askopenfilename(initialdir = "../",title = "Select a File",filetypes = (("CSV","*.csv*"),("all files","*.*")))) as csvfile:
            lines = csv.reader(csvfile, delimiter=';')
            for row in (lines):
                x.append(int(row[2]))
                y.append(int(row[1]))

        plt.figure(1)
        plt.plot(x, y, color = 'g', linestyle = 'None',marker = 'o',label = "Test")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Y en fonction de X', fontsize = 20)
        plt.grid()
        plt.legend()
        plt.show()
    
    def new_graph_xt(self):
        x = []
        y = []
  
        with open(filedialog.askopenfilename(initialdir = "../",title = "Select a File",filetypes = (("CSV","*.csv*"),("all files","*.*")))) as csvfile:
            lines = csv.reader(csvfile, delimiter=';')
            for row in (lines):
                y.append(int(row[1]))
                x.append(int(row[0]))

        plt.figure(2)
        plt.plot(x, y, color = 'g', linestyle = 'dashed' ,marker = 'o',label = "Test")
        plt.xlabel('T')
        plt.ylabel('X')
        plt.title('X en fonction de T', fontsize = 20)
        plt.grid()
        plt.legend()
        plt.show()

    def new_graph_yt(self):
        x = []
        y = []
  
        with open(filedialog.askopenfilename(initialdir = "../",title = "Select a File",filetypes = (("CSV","*.csv*"),("all files","*.*")))) as csvfile:
            lines = csv.reader(csvfile, delimiter=';')
            for row in (lines):
                x.append(int(row[0]))
                y.append(int(row[2]))


        plt.figure(3)
        plt.plot(x, y, color = 'g', linestyle = 'dashed',marker = 'o',label = "Test")
        plt.xlabel('T')
        plt.ylabel('Y')
        plt.title('Y en fonction de T', fontsize = 20)
        plt.grid()
        plt.legend()
        plt.show()