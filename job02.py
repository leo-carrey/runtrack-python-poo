class Livre:
    def __init__(self, titre, auteur, nombre_depages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_depages = nombre_depages

    def modif_titre(self, titre):
        self.__titre = titre
        return self.__titre
    
    def modif_auteur(self, auteur):
        self.__auteur = auteur
        return self.__auteur
    
    def modif_nombre_depages(self, nombre_depages):
        if nombre_depages == int(nombre_depages) and nombre_depages > 0:
            self.__nombre_depages = nombre_depages
        else:
            print("veuillez inserer un nombre entier positif !!!")
        return self.__nombre_depages
        
    def afficher(self):
        return f'le livre se nomme {self.__titre}, il a pour auteur {self.__auteur} et a {self.__nombre_depages} pages'
    
livre = Livre("Les miss","Jean",1)
livre.modif_titre("Les misérables")
livre.modif_auteur("Jean Valjean")
print(livre.modif_nombre_depages(288))
print(livre.afficher())