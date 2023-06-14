class ListeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def afficher(self):
        print("Liste des tâches ménagères :")
        for i, tache in enumerate(self.taches):
            print(f"{i+1}. ", end="")
            tache.afficher()

    def choisir_tache(self):
        choix = input("Choisissez le numéro de la tâche à exécuter compris entre 1 et 4  : ")
        try:
            choix = int(choix)
            if 1 <= choix <= len(self.taches):
                tache = self.taches[choix - 1]
                tache.executer()
                choix = input("Voulez-vous continuer oui(o) ou non(n) : ")
                if choix.lower() == 'o':
                    print("\n Merci d'avoir utiliser notre application \n")
                    return False
                else:
                    print("Merci \n")
            else:
                print("Choix invalide.")
        except ValueError:
            print("Choix invalide.")
        return True
