# Importe les classes et fonctions nécessaires depuis les modules Niveau et fenetre
from Niveau import *
from fenetre import *

# Crée une instance de la classe Niveau
niveau = Niveau()

# Initialise le niveau
niveau.initialisation()

# Appelle une fonction (à remplacer avec la vraie implémentation)
initialisation(30)

# Crée une fenêtre avec une largeur de 580 pixels et une hauteur de 350 pixels
fenetre(580, 350)

# Boucle pour chaque tube de boules du joueur dans le niveau
for i, tube in enumerate(niveau.boules_joueur):
    """
    Affiche une image représentant un tube vide à une position spécifique.
    """
    afficher_image(60 + i * 80, 30, "sprites_balle/tube_vide.png")

    # Boucle pour chaque boule dans le tube
    for j, boule in enumerate(tube.afficher_elements()):
        """
        Affiche une image représentant une boule de la couleur correspondante
        à une position spécifique dans le tube.
        """
        afficher_image(60 + i * 80 + 10, 35 + j * 40, "sprites_balle/{}.png".format(boule.get_couleur().lower()))

# Appelle une fonction (à remplacer avec la vraie implémentation)
tick()

"""
Attend l'appui sur Entrée pour terminer le programme.
"""
input("Terminer en appuyant sur Entrée")

