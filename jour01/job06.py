class Animal:
    def __init__(self, prenom):
        self.age = 0
        self.prenom = prenom

    def Viellir(self):
        print(self.age)
        self.age += 1
        return self.age
    
    def Nommer(self, prenom):
        self.prenom = prenom
    
    def print_everything(self):
        return f'Le nom est {self.prenom} et son age et de {self.age}'
    
A = Animal("prenom")
print(A.Viellir())
A.Nommer('salameche')
print(A.print_everything())