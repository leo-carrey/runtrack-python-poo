class Livre:
    def __init__(self, titre, auteur, nombre_depages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_depages = nombre_depages

    def modif_titre(self, titre):
        self._titre = titre
        return self._titre
    
    def modif_auteur(self, auteur):
        self._auteur = auteur
        return self._auteur
    
    def modif_nombre_depages(self, nombre_depages):
        self._nombre_depages = nombre_depages
        if nombre_depages != int(nombre_depages):
            self._nombre_depages = 0
            print("veuillez inserer un nombre entier positif !!!")
        return self._nombre_depages
        
    def afficher(self):
        return f'le livre se nomme {self._titre}, il a pour auteur {self._auteur} et a {self._nombre_depages} pages'
    
livre = Livre("Les miss","Jean",1)
livre.modif_titre("Les misérables")
livre.modif_auteur("Jean Valjean")
print(livre.modif_nombre_depages(288.1))
print(livre.afficher())