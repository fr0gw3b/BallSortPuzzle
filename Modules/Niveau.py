# Module de niveaux
    # Tom
from Tube import Tube
from Boule import Boule
import fenetre

import random

class Niveau:
    def __init__(self):
        self.niveau = 0
        self.boules_par_defaut = [];
        self.boules_joueur = [];
        
        self.tube_selectionne = None;

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

    def reinitialisation(self):
        nouvelles_boules_joueur = []
        for tube in self.boules_par_defaut:
            nouveau_tube = Tube()
            for boule in tube.elmts:
                nouvelle_boule = Boule(boule.get_couleur())
                nouveau_tube.empiler(nouvelle_boule)
            nouvelles_boules_joueur.append(nouveau_tube)

        self.boules_joueur = nouvelles_boules_joueur
        self.afficher_niveau()
    
    def deplacer_boule(self, tube_source, tube_destination):
        if tube_source.est_vide():
            print("Le tube source est vide. Sélectionnez un autre tube.")
            return

        boule_a_deplacer = tube_source.depiler()

        if not tube_destination.est_vide():
            boule_en_haut = tube_destination.recuperer_elements(-1)
            if boule_a_deplacer.get_couleur() != boule_en_haut.get_couleur():
                print("Impossible de déplacer la boule. Les couleurs ne correspondent pas.")
                tube_source.empiler(boule_a_deplacer)
                return

        if not tube_destination.est_plein():
            tube_destination.empiler(boule_a_deplacer)


    def afficher_niveau(self):
        for i, tube in enumerate(self.boules_joueur):
            fenetre.afficher_image(60 + i * 80, 30, "sprites/tube_vide.png")

            for j, boule in enumerate(tube.afficher_elements()):
                fenetre.afficher_image(60 + i * 80 + 10, 35 + j * 40, "sprites/{}.png".format(boule.get_couleur().lower()))
