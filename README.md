
TUBES :
	
 	- pile_vide(): Créer une pile vide

	- est_vide(p): Teste si la pile p est vide (renvoie un booléen)

	- empiler(p,x): Ajoute un élément 'x' au sommet du tube, à condition que le tube ne soit pas plein.
				Lance une IndexError avec le message "La pile est plaine" si le tube est plein.

	- depiler(p):  Retire et renvoie l'élément en haut du tube, à condition que le tube ne soit pas vide.
				Lance une IndexError avec le message "La pile est vide" si le tube est vide.

	- est_plein(): Teste si la pile p est pleine (renvoie un booléen)

	- new_maxi(x): Cette méthode permet de changer la capacité maximale du tube.
				Paramètres :
        	   		- x : Nouvelle capacité maximale à définir pour le tube.

	-afficher_elements(): Renvoie la liste des éléments actuellement présents dans le tube.

	-recuperer_elements(index): Permet de selectionner un element en particulier et l'affiche






FENETRE :

	-fenetre(largeur, hauteur):Déploie une fenêtre à partir d'une hauteur et d'une largeur.
    					    Nécessaire pour les fonction afficher_image, dernier_clic, derniere_touche

	-initialisation(fps): Initialise le lancement d'un jeu et fixe le fps max

	-afficher_image(x, y, nom_fichier): Affiche une image aux coordonnées (x, y) de la fenetre ouverte à l'appel de la fonction fenetre

	-refresh_control(): Fonction interne au module. Ne pas utiliser.

	-dernier_clic(): Récupère les coordonnées du dernier clic de l'utilisateur depuis le dernier appel à la fonction tick.
    				Retour : None s'il n'y a pas eu de clic ou (x, y) sinon.
    				Remarque : (0, 0) est en bas à gauche, x en abcisse.

	-derniere_touche(): Renvoie la dernière touche appuyée par l'utilisateur depuis le dernierappel à la fonction tick.
    				 Retour : None s'il n'y a pas eu de touche d'appuyée, ou un str représentantla touche sinon (une lettre si c'est une touche du clavier, ou "haut","bas", "droite" ou "gauche" si c'est une touche fléchée.

	-tick(): Permet la synchronisation du jeu au FPS fixé à l'appel de "initialisation" ainsi que de réinitialiser la recherche d'entrée utilisateur (clic ettouche). 
		 Doit être appelé une fois par frame.

	-est_fini(): Indique si la fenetre de jeu a été fermée.

	-terminer(): Permet de quitter proprement le module de l'interface graphique.
    		 À appeler avant la fin du programme de préférence.






NIVEAUX :

	- deplacer_boule : Permet de faire passer une boule d'un tube à l'autre

	- reinitialisation(): Permet de remettre recommencer le niveaux en générant un nouveaux niveaux

	- initialisation(): Créer plusieurs tubes et insère des boules de couleurs aléatoires dans les tubes, mais laisse 2 tubes vides

	- afficher_niveau: Permet d'afficher l'etat actuel du niveaux





VUE :



JEU : 



BOULE :

	-get_couleur(self): Renvoie la couleur de la boule.






IMPORTS : 

	-Tube: Importe le module Tube pour pouvoir manipuler piles

	-Boule: Importe le module Boule pour pouvoir manipuler des boules en générant un objet Boule avec une couleur 

	-fenetre: Importe le module fenetre pour utiliser l'interface graphique de pygame

	-Niveaux: Importe le module Niveuax pour pouvoir générer un niveaux aléatoire composé de tubes et de boules

	-Random: Importe le module random pour pouvoir générer des nombres aléatoire

	-pygame: Gestionnaire d'interface graphique minimal.
