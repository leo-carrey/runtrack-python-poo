class Vehicule:
    def __init__(self, marque, annee, prix, modele):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele

    def informationsVehicule(self):
        return f'Marque : {self.marque}\nModel : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}\n'
    
    def demarrer(self):
        return 'Atention je roule\n'

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, modele):
        super().__init__(marque, annee, prix, modele)
        self.portes = 4

    def informationsVehicule(self):
        return f'Marque : {self.marque}\nModel : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}\nNombre de Portes : {self.portes}\n'

    def demarrer(self):
        return 'Atention je roule en voiture\n'

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, modele):
        super().__init__(marque, annee, prix, modele)
        self.roue = 2

    def informationsVehicule(self):
        return f'Marque : {self.marque}\nModel : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}\nNombre de Roue : {self.roue}\n'
    
    def demarrer(self):
        return 'Atention je roule en moto\n'

voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
print(voiture.informationsVehicule())
print(voiture.demarrer())
print(moto.informationsVehicule())
print(moto.demarrer())