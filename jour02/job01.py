class Rectangle:
    def __init__(self, longueur, largueur):
        self.__longueur = longueur
        self.__largeur = largueur

    def modif_longueur(self, longueur):
        self.__longueur = longueur
        return self.__longueur
    
    def modif_largueur(self, largueur):
        self.__largeur = largueur
        return self.__largeur
    
    def afficher(self):
        return f'la longueur du triangle est de {self.__longueur} et a une largueur de {self.__largeur}'
    
rectangle = Rectangle(10,5)
print(rectangle.modif_longueur(5))
print(rectangle.modif_largueur(3))
print(rectangle.afficher())