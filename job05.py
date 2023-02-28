class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def demarrer(self):
        if self.verifier_plein() > 5:
            self.__en_marche = True
        return self.__en_marche

    def arreter(self):
        self.__en_marche = False
        return self.__en_marche

    def verifier_plein(self):
        return self.__reservoir
    
    def get_info(self):
        return f'la marque de la voiture se nomme {self.__marque}\nle model de la voiture est {self.__modele}\nla voiture a été créé en {self.__annee}\net elle a {self.__kilometrage} kilomètre\n'
    
    def set_voiture(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage


voiture = Voiture("cupra", "Formentor", 2021, 2000)
print(voiture.verifier_plein())
print(voiture.demarrer())
print(voiture.arreter())
print(voiture.get_info())
voiture.set_voiture("cupra", "Formentor", 2021, 51060)
print(voiture.get_info())