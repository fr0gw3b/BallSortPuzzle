class Tube:
    def __init__(self):
        """
        Initialise un objet Tube avec une liste vide pour stocker les éléments et une capacité maximale fixée à 4.
        """
        self.elmts = []
        self.maxi = 4

    def est_vide(self):
        """
        Vérifie si le tube est vide.

        Retourne True si le tube est vide, et False sinon.
        """
        return self.elmts == []

    def empiler(self, x):
        """
        Ajoute un élément 'x' au sommet du tube, à condition que le tube ne soit pas plein.

        Lance une IndexError avec le message "La pile est plaine" si le tube est plein.
        """
        if self.est_plein():
            raise IndexError("La pile est plaine")
        else:
            self.elmts.append(x)

    def depiler(self):
        """
        Retire et renvoie l'élément en haut du tube, à condition que le tube ne soit pas vide.

        Lance une IndexError avec le message "La pile est vide" si le tube est vide.
        """
        if self.est_vide():
            raise IndexError("La pile est vide")
        return self.elmts.pop()

    def est_plein(self):
        """
        Vérifie si le tube est plein, c'est-à-dire si le nombre d'éléments atteint la capacité maximale.

        Retourne True si le tube est plein, et False sinon.
        """
        return len(self.elmts) == self.maxi

class Tube:
    # ... (les autres méthodes restent inchangées)

    def new_maxi(self, x):
        """
        Modifie la capacité maximale du tube.

        Paramètres :
        - x : Nouvelle capacité maximale à définir pour le tube.

        Cette méthode permet de changer la capacité maximale du tube.
        """
        self.maxi = x

    def afficher_elements(self):
        """
        Renvoie la liste des éléments actuellement présents dans le tube.
        """
        return self.elmts
