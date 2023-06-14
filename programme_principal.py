from tache import Tache
from liste_taches import ListeTaches

class ProgrammePrincipal:
    def __init__(self):
        self.liste_taches = ListeTaches()

    def executer(self):
        tache1 = Tache("Laver la vaisselle", "\nEtape 1 : Remplir l'évier d'eau savonneuse,\nEtape 2 : laver chaque article,\nEtape 3 : les rincer.")
        tache2 = Tache("Passer l'aspirateur", "\nEtape 1 : Brancher l'aspirateur,\nEtape 2 : passer l'aspirateur dans chaque pièce en faisant des mouvements réguliers.")
        tache3 = Tache("Faire la lessive", "\nEtape 1 : Séparer les vêtements par couleur,\nEtape 2 : mettre les vêtements dans la machine à laver,\nEtape 3 : ajouter de la lessive \nEtape 4 : lancer le cycle de lavage.")
        tache4 = Tache("Nettoyer les vitres", "\nEtape 1 : Vaporiser un nettoyant pour vitres sur la surface,\nEtape 2 : essuyer avec un chiffon propre \nEtape 3 : sec jusqu'à ce que les vitres soient propres.")


        self.liste_taches.ajouter_tache(tache1)
        self.liste_taches.ajouter_tache(tache2)
        self.liste_taches.ajouter_tache(tache3)
        self.liste_taches.ajouter_tache(tache4)

        for _ in range(3):
            self.liste_taches.afficher()
            continuer = self.liste_taches.choisir_tache()
            if not continuer:
                break

if __name__ == "__main__":
    print("              ************ BIENVENUE SUR GES-TACHES ************\n")
    print("              Le gestionnaire des tâches menagères.\n")
    programme = ProgrammePrincipal()
    programme.executer()
