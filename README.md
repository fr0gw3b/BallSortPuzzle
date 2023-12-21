# Class Ball 
TUBES :
pile_vide(): créer une pile vide
est_vide(p): teste si la pile p est vide (renvoie un booléen)
empiler(p,x): ajoute l'élément x au sommet de la pile p
depiler(p): retire l'élément x du sommet de la pile et le renvoie
est_plein(): teste si la pile p est pleine (renvoie un booléen)
new_maxi(): définit une une nouvelle valeur max de la pile 


NIVEAUX :
recuperer_niveau(): recupere le niveaux actuel 
reinitialisation(): permet de remettre le niveau à l'état d'origine
niveau_suivant(): permet d'acceder au prochain niveaux apres une victoire 
initialisation(): génère un niveaux avec des tubes,boules de couleurs
recuperer_tube(tube): permet de selectionner le tube (tube)


INTERFACE GRAPHIQUE :
initialisation(): définit le niveaux
fenetre(l,h): génère une fenetre de largeur l et de hauteur h
afficher_image(x,y,nom_fichier): affiche une image grâce à son nom (nom_fichier) au coordonnées d'abscice x et d'ordonnée y 
dernier_clic(): récupere la position du dernier clic du joueur
