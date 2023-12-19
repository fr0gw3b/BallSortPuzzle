# Module de niveaux
    # Tom
from Tube import Tube
from Boule import Boule
import random

class Niveau:
    def __init__(self):
        self.niveau = 0
        self.boules_par_defaut = [];
        self.boules_joueur = [];

        # Définition des couleurs des boules obtenables
        self.couleurs_list = [ "Rouge", "Bleu", "Vert", "Jaune", "Turquoise", "Violet", "Orange" ]
    
    def initialisation(self):
        # Initialiser le niveaux
            # -> Créer plusieurs tubes
            # -> Insérer des boules de couleurs aléatoires dans les tubes, mais laisser 2 tubes vides
        
        couleurs_aleatoires = random.sample(self.couleurs_list, 4)
        couleurs_melangees = []

        for i in range(6):
            if not couleurs_melangees:
                couleurs_melangees = couleurs_aleatoires + couleurs_aleatoires
                random.shuffle(couleurs_melangees)

            nouveau_tube = Tube()
            if i >= 4:
                # Tubes vides
                self.boules_par_defaut.append(nouveau_tube)
            else:
                # Tubes avec des boules
                for k in range(4):
                    couleur_boule = couleurs_melangees.pop()
                    nouvelle_boule = Boule(couleur_boule)
                    nouveau_tube.empiler(nouvelle_boule)
                self.boules_par_defaut.append(nouveau_tube)

        self.boules_joueur = self.boules_par_defaut

        """for i, tube in enumerate(self.boules_par_defaut):
            print(f"Tube {i + 1}:")
            elements_du_tube = tube.afficher_elements()
            for index, boule in enumerate(elements_du_tube):
                print(f"   Boule {index + 1}: Couleur = {boule.get_couleur()}")"""

    def reinitialisation(self):
        self.boules_joueur = self.boules_par_defaut

    def recuperer_niveau(self):
        return self.niveau

    def recuper_tube(self, tube):
        pass

    def niveau_suivant(self):
        pass
