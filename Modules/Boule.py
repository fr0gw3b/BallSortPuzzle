class Boule:
    def __init__(self, couleur):
        """
        Initialise un objet Boule avec une couleur spécifiée.

        Paramètres :
        - couleur : Couleur de la boule.

        La couleur de la boule est définie lors de l'initialisation de l'objet.
        """
        self.couleur = couleur

    def get_couleur(self):
        """
        Renvoie la couleur de la boule.
        """
        return self.couleur
