"""
Gestionnaire d'interface graphique minimal.
"""

import pygame

#####################
# Variables globales
##

# Frame Per Second
FPS = 30
clock = None

# Images préchargées
images = {}

# Information sur les entrées utilisateur
last_clic = None
last_key = None
termine = False

############
# Fonctions
##

def initialisation(fps):
    """
    Initialise le lancement d'un jeu et fixe le fps max
    """
    global FPS, clock
    pygame.init()
    FPS = fps
    clock = pygame.time.Clock()

    
def fenetre(largeur, hauteur):
    """
    Déploie une fenêtre à partir d'une hauteur et d'une largeur.
    Nécessaire pour les fonction afficher_image, dernier_clic, derniere_touche
    """
    pygame.display.set_mode((largeur, hauteur))
    

def afficher_image(x, y, nom_fichier):
    """
    Affiche une image aux coordonnées (x, y) de la fenetre ouverte à l'appel
    de la fonction fenetre
    """
    (largeur, hauteur) = pygame.display.get_surface().get_size()
    y = hauteur - y
    
    # mémoisation de l'image
    if not nom_fichier in images:
        images[nom_fichier] = pygame.image.load(nom_fichier).convert()
    
    img = images[nom_fichier]
    (_, h) = img.get_size()
    pygame.display.get_surface().blit(img, (x, y - h))
    
def refresh_control():
    """
    Fonction interne au module. Ne pas utiliser.
    """
    global last_clic, last_key, termine
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Fin du jeu
            termine = True
        elif event.type == pygame.KEYDOWN:
            if event.__dict__["key"] == 1073741903:
                last_key = "droite"
            elif event.__dict__["key"] == 1073741904:
                last_key = "gauche"
            elif event.__dict__["key"] == 1073741905:
                last_key = "bas"
            elif event.__dict__["key"] == 1073741906:
                last_key = "haut"
            else:
                last_key = event.unicode
        elif event.type == pygame.MOUSEBUTTONUP:
            (x, y) = event.__dict__["pos"]
            (largeur, hauteur) = pygame.display.get_surface().get_size()
            last_clic = (x, hauteur - y) # renversement de l'axe y

def dernier_clic():
    """
    Récupère les coordonnées du dernier clic de l'utilisateur depuis
    le dernier appel à la fonction tick.
    Retour : None s'il n'y a pas eu de clic ou (x, y) sinon.
    Remarque : (0, 0) est en bas à gauche, x en abcisse.
    """
    refresh_control()
    return last_clic

def derniere_touche():
    """
    Renvoie la dernière touche appuyée par l'utilisateur depuis le dernier
    appel à la fonction tick.
    Retour : None s'il n'y a pas eu de touche d'appuyée, ou un str représentant
    la touche sinon (une lettre si c'est une touche du clavier, ou "haut",
    "bas", "droite" ou "gauche" si c'est une touche fléchée.
    """
    refresh_control()
    return last_key
    
def tick():
    """
    Permet la synchronisation du jeu au FPS fixé à l'appel de "initialisation"
    ainsi que de réinitialiser la recherche d'entrée utilisateur (clic et
    touche). Doit être appelé une fois par frame.
    """
    global last_key, last_clic, clock, FPS
    last_key = None
    last_clic = None
    pygame.display.flip() # transition bufferisée
    clock.tick(FPS)

def est_fini():
    """
    Indique si la fenetre de jeu a été fermée.
    """
    return termine
    
def terminer():
    """
    Permet de quitter proprement le module de l'interface graphique.
    À appeler avant la fin du programme de préférence.
    """
    pygame.quit()

