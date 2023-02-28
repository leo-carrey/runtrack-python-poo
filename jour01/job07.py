class Personnage:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1
    
    def haut(self):
        self.y += 1
    
    def bas(self):
        self.y -= 1

    def print_everything(self):
        pos=(self.x,self.y)
        return f'Position is {pos}' 
    
p = Personnage(0,0)
p.gauche()
p.gauche()
p.bas()
p.droite()
p.haut()
print(p.print_everything())