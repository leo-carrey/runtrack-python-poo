class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTache:
    def __init__(self, taches):
        self.taches = taches

    def ajouterTache(self, tache):
        if tache not in self.taches:
            self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self,tache):
        tache.statut = "Fini"

    def afficherListe(self):
        for tache in self.taches:
            print(f'Titre : {tache.titre} | Description : {tache.description} | Statut : {tache.statut}')

    def filterListe(self, statut):
        for tache in self.taches:
            if tache.statut == statut:
                print(f'Titre : {tache.titre} | Description : {tache.description} | Statut : {tache.statut}')

tache1 = Tache("tache1","faire la tache2","fini")
tache2 = Tache("tache2","faire la tache3","à faire")
tache3 = Tache("tache3","faire la tache4","à faire")
tache4 = Tache("tache4","faire la tache1","à faire")
liste = ListeDeTache([tache1,tache2,tache3])

liste.ajouterTache(tache4)
liste.marquerCommeFinie(tache2)
liste.afficherListe()
liste.filterListe("à faire")
liste.supprimerTache(tache1)
liste.afficherListe()