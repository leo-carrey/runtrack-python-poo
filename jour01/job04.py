class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("je suis " + self.nom +" "+ self.prenom)

p1 = Personne("John", "Doe")
p2 = Personne("Jean", "Dupond")
p1.SePresenter()
p2.SePresenter()
