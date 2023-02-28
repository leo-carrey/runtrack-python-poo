class Produit:
    def __init__(self,nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT +(self.prixHT * self.TVA)
    
    def Afficher(self):
        return f'le nom du produit est {self.nom} et son prix TTC est {self.CalculerPrixTTC()}'
    
    def changer_prix_nom(self, nom, prixHT):
        self.nom = nom
        self.prixHT = prixHT
    
    def Afficher_nom(self):
        return self.nom

    def Afficher_prix(self):
        return self.prixHT
    
Produit.TVA = 0.2 

pomme = Produit("pomme", 3, Produit.TVA)
banane = Produit("banane", 6, Produit.TVA)
print(pomme.Afficher())
print(banane.Afficher())
banane.changer_prix_nom("big banane", 12)
print(banane.Afficher())
print(pomme.Afficher_nom())
print(pomme.Afficher_prix())