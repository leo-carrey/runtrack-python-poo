class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur

    def aire(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14 * self.radius**2
   
rectangle = Rectangle(5,10)
cercle = Cercle(2)

print(rectangle.aire())
print(cercle.aire())