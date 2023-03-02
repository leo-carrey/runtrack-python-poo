class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        return self.age
    
    def Bonjours(self):
        return "Hello"
    
    def ModifAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours():
        return "je vais en cours"
    
    def afficherAge(self):
        return f"j'ai {self.age} ans"
    
class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        return "Le cours va commencer"
    
p1 = Personne()
eleve = Eleve()
professeur = Professeur("mathematique")

print(eleve.afficherAge())
print(eleve.Bonjours())
eleve.ModifAge(15)
professeur.ModifAge(40)
print(professeur.Bonjours())
print(professeur.enseigner())