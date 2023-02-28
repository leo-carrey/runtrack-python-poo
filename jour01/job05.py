class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def AfficherLesPoints(self):
        return self.x, self.y
    
    def AfficherX(self):
        return self.x

    def AfficherY(self):
        return self.y
    
    def ChangerX(self, X):
        self.x = X

    def ChangerY(self, Y):
        self.y = Y

p = Point(1,2)

print(p.AfficherLesPoints())
print(p.AfficherX())
print(p.AfficherY())
p.ChangerX(4)
p.ChangerY(5) 
print(p.AfficherLesPoints())