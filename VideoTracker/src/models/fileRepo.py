from tkinter import *
from tkinter import filedialog

class FileRepo:
    
    def __init__(self,filename,fileContent):
        """Initialise les caracteristiques"""
        self.__filename = filename
        self.__fileContent = fileContent
    
    
    def saveFile(self,filename:str,fileContent:str)->None:
        """Sauvegarde le fichier avec le contenu donné en entré"""
        
        file_path = filedialog.asksaveasfilename(
        title="Sauvegarder le fichier",
        filetypes=[("Fichiers CSV", "*.csv")],
        initialdir="/",)
        if file_path:
            if not file_path.endswith(".csv"):
                file_path += ".csv"
            with open(file_path, "w") as f:
                f.write(fileContent)
    
    def dataToCSV(listOfPoints: list) -> str:
        """Converts a list of points to CSV format with the separator ';'"""

        count = 0
        lign = []

        for elt in listOfPoints:
            if elt is not None:
                lign.append(str(count) + ';' + str(elt[0]) + ';' + str(elt[1]) + '\n')
                count += 1

        CSVfile = ''
        for element in lign:
            CSVfile += element

        return CSVfile
