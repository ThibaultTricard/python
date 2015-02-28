GAUCHE_PLATEAU=0
DROITE_PLATEAU=10
BAS_PLATEAU=22

class Forme():

    def __init__(self, pos1, pos2, form):
        self.pos1 = pos1 #bloc haut gauche
        self.pos2 = pos2 #bloc bas droite
        self.form = form #dictionnaire comment est tournee la forme
        self.formActuelle = 0 #la forme est droite

    def gauche(self):
        if (self.pos1[1] > GAUCHE_PLATEAU):
            self.pos1[1] = self.pos1[1] - 1
            self.pos2[1] = self.pos2[1] - 1

    def droite(self):
        if (self.pos2[1] < DROITE_PLATEAU):
            self.pos1[1] = self.pos1[1] + 1
            self.pos2[1] = self.pos2[1] + 1

    def bas(self):
        if self.pos2[0] < BAS_PLATEAU:
            self.pos1[0] = self.pos1[0] + 1
            self.pos2[0] = self.pos2[0] + 1

    def tourner(self):
        if self.formActuelle == 3 :
            self.formActuelle = 0
        else :
            self.formActuelle = self.formActuelle + 1
            
            
            
        """todo"""
        """calculer et verifier la pos2"""
