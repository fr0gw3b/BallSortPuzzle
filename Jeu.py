import fenetre
from Niveau import *

fenetre.initialisation(30)
fenetre.fenetre(580,350)
fenetre.afficher_image(0, 0, "sprites/fond.png")

# Initialisation du modèle
niveau = Niveau()
niveau.initialisation()

niveau.afficher_niveau()

fenetre.afficher_image(250, 300, "sprites/reset.png")

clic_sur_reset = False

# Boucle de jeu principale
# Boucle de jeu principale
while not fenetre.est_fini():
    # Mise à jour de l'affichage et des entrées utilisateur

    clic = fenetre.dernier_clic()
    niveau.afficher_niveau()

    if clic:

        # Vérifiez si on clique sur le bouton reset
        if 250 <= clic[0] <= 250 + 250 and 300 <= clic[1] <= 300 + 300:
            clic_sur_reset = True
        else:
            # Vérifiez si le clic est à l'intérieur de la zone des tubes
            for i, tube in enumerate(niveau.boules_joueur):
                if 60 + i * 80 <= clic[0] <= 60 + (i + 1) * 80 and 30 <= clic[1] <= 30 + 4 * 40:
                    if niveau.tube_selectionne is None:
                        niveau.tube_selectionne = i
                    else:
                        niveau.deplacer_boule(niveau.boules_joueur[niveau.tube_selectionne], tube)
                        niveau.tube_selectionne = None

    fenetre.tick()

    # Réinitialisez le niveau si le bouton reset a été activé
    if clic_sur_reset:
        niveau.reinitialisation()
        clic_sur_reset = False

# Terminaison propre
fenetre.terminer()
