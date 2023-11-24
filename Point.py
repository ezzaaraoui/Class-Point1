import math
class Point :

    def __init__(self, abscisse = 0, ordonne = 0):
        self.abscisse = abscisse
        self.ordonne = ordonne

    def get_abscisse(self):
        return self.abscisse

    def set_abscisse(self,new_abscisse):
        self.abscisse = new_abscisse
        

    def get_ordonne(self):
        return self.ordonne

    def set_ordonne(self,new_ordonne):
        self.ordonne = new_ordonne


    def Distance(self, point):
        dx = self.abscisse - point.get_abscisse()
        dy = self.ordonne - point.get_ordonne()
        return math.sqrt(dx**2 + dy**2)


    def norme(self):
        return math.sqrt(self.abscisse**2 + self.ordonne**2)

    



    
