class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
        
    def circonference(self):
        return self.rayon*2*3.14
    
    def aire(self):
        return 3.14*self.rayon**2
    
    def diametre(self):
        return 2*self.rayon**2
    
    def print_everything(self):
        return f'le cercle de rayon {self.rayon}\na pour circonference {self.circonference()},\nun diametre de {self.diametre()}\net une aire de {self.aire()}'
    
cercle_4=Cercle(4)
print(cercle_4.print_everything())
cercle_7=Cercle(7)
print(cercle_7.print_everything())