class Point:
    
    def __init__(self,x,y):
        """Initialise les caracteristiques du point"""
        self.__x = x
        self.__y = y
        
    def getx(self):
        """Recupere la coordonne x"""
        
        return self.__x
    
    def gety(self):
        """Recupere la coordonne y"""
        
        return self.__y

        