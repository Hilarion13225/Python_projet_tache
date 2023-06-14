class Tache:
    def __init__(self, nom, methode):
        self.nom = nom
        self.methode = methode

    def afficher(self):
        print(f"- {self.nom}")

    def executer(self):
        print(f"\nExécuter la tâche : {self.nom}\n")
        print(f"Méthode : {self.methode}\n")
        
