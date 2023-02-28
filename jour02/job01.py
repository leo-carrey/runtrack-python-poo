class Rectangle:
    def __init__(self, longueur, largueur):
        self._longueur = longueur
        self._largeur = largueur

    def modif_longueur(self, longueur):
        self._longueur = longueur
        return self._longueur
    
    def modif_largueur(self, largueur):
        self._largeur = largueur
        return self._largeur
    
rectangle = Rectangle(10,5)
print(rectangle.modif_longueur(5))
print(rectangle.modif_largueur(3))