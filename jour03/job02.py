class CompteBancaire:
    def __init__(self,compte, nom, prenom, solde, decouvert):
        self.__compte = compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        return f'Numéro de compte :{self.__compte}\nNom :{self.__nom}\nPrenom :{self.__prenom}\nSolde :{self.__solde}'
    
    def afficherSolde(self):
        return f'Solde du compte :{int(self.__solde)}'
    
    def versement(self, versement):
        self.__solde += int(versement)
        return f'Solde du compte :{int(self.__solde)}'

    def retrait(self,montant):
        if montant <= self.__solde or self.__decouvert == True:
            self.__solde -= int(montant)
            return f'Solde du compte :{int(self.__solde)}'
        else:
            return "veuillez entrer un montant valide"
        
    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.5
        return f'Solde du compte :{int(self.__solde)}'
    
    
    def virement(self, montant, compte):
        userinput = input("écrivez oui pour confirmer le virement :")
        if userinput == "oui":
            if montant < self.__solde:
                self.__solde -= montant
                compte.__solde += montant
                return f"Le virement de {montant} euros a été effectué avec succès. Nouveau solde : {int(self.__solde)} euros."
        else:
            return "erreur"

            
hugo = CompteBancaire(6969,"andriamaromanana", "hugo", 13000, True)
Jhon = CompteBancaire(1203, "Doe", "Jhon", -1200, True)

print(hugo.afficher())
print(hugo.afficherSolde())
print(hugo.versement(12000))
print(hugo.retrait(26000))
print(hugo.agios())
print(hugo.versement(15000))
print(hugo.virement(2000,Jhon))
print(hugo.afficherSolde())
print(Jhon.afficherSolde())