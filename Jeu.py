from Niveau import *
from fenetre import *

niveau = Niveau()
niveau.initialisation()

initialisation(30)
fenetre(580,350)

for i, tube in enumerate(niveau.boules_joueur):
    afficher_image(60 + i * 80, 30, "sprites_balle/tube_vide.png")

    for j, boule in enumerate(tube.afficher_elements()):
        afficher_image(60 + i * 80 + 10, 35 + j * 40, "sprites_balle/{}.png".format(boule.get_couleur().lower()))

tick()
input("terminer en appuyant sur entrée")
