class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur

    def aire(self):
        return self.largeur * self.hauteur
    
rectangle = Rectangle(5,10)
print(rectangle.aire())