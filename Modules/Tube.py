# Cody

class Tube:
    def __init__(self, x):
        self.elmts = []
        self.maxi = x

    def est_vide(self):
        return self.elmts == []

    def empiler(self, x):
        if self.est_plein():
            raise IndexError ("La pile est plaine")
        else :
            self.elmts.append(x)

    def depiler (self):
        if self.est_vide():
            raise IndexError ("La pile est vide")
        return self.elmts.pop()

    def est_plein(self):
        return len(self.elmts) == self.maxi

    def new_maxi(self, x):
        self.maxi = x
