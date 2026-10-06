from random import *
import sys
sys.path.append("../")
from src.models.point import *
from src.models.fileRepo import *

def randomPoints(n:int)->list:
    #permet de construire une liste avec n points qui ont des coordonnées aléatoires.
    lPoints = []
    for i in range(n):
        rdPoint = Point(randint(-200,200),randint(-200,200))
        lPoints.append((rdPoint.getx(),rdPoint.gety()))
    
    return lPoints


u = randomPoints(15)
contenuDuCSV = FileRepo.dataToCSV(u)
FileRepo.saveFile('CSVtest.csv',contenuDuCSV)

with open('CSVtest.csv','r') as f:
    print(f.read())     
    