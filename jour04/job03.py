class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return self.__largeur + self.__longueur * 2

    def surface(self):
        return self.__longueur * self.__largeur
    
    def get(self):
        return f'la longueur du rectangle : {self.__longueur}\nla largeur de rectangle : {self.__largeur}'
    
    def set(self, longueur, largeur):
        self.__largeur = largeur
        self.__longueur = longueur

class Parallelepipede(Rectangle):
    def __init__(self,longueur,largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return self.surface() * self.hauteur
    
rectangle1 = Rectangle(15,10)
p = Parallelepipede(15,10,5)

print(rectangle1.perimetre())
print(rectangle1.surface())
rectangle1.set(20,5)
print(rectangle1.get())
print(p.volume())