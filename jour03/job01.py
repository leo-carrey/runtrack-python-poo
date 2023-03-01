class Ville():
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def set_ville(self):
        self.__nb_habitants += 1

    def get_ville(self):
        return f'Population de la ville de {self.__nom}: {self.__nb_habitants} habitants'

class Personne:
    def __init__(self, nom, age, objet_ville):
        self.__nom = nom
        self.__age = age
        self.__objet_ville = objet_ville

    def ajouterPopulation(self):
        self.__objet_ville.set_ville()

    def set_personne(self, nom, age, objet_ville):
        self.__nom = nom
        self.__age = age
        self.__objet_ville = objet_ville

    def get_personne(self):
        return self.__nom,self.__age, self.__objet_ville


ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)
Jhon = Personne("John", 45,ville1)
Myrtille = Personne("Myrtille", 4, ville1)
Chloe = Personne("Chloé", 18,ville2)

print(ville1.get_ville())
print(ville2.get_ville())

Jhon.ajouterPopulation()
Myrtille.ajouterPopulation()
Chloe.ajouterPopulation()

print(ville1.get_ville())
print(ville2.get_ville())