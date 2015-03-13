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
        #on fait bouger le block d'une case vers la gauche
        if (self.pos1[1] > GAUCHE_PLATEAU):
            self.pos1[1] = self.pos1[1] - 1
            self.pos2[1] = self.pos2[1] - 1

    def droite(self):
        #on fait bouger le block d'une case vers la droite
        if (self.pos2[1] < DROITE_PLATEAU):
            self.pos1[1] = self.pos1[1] + 1
            self.pos2[1] = self.pos2[1] + 1

    def bas(self):
        #on fait bouger le block d'une case vers le bas
        if self.pos2[0] < BAS_PLATEAU:
            self.pos1[0] = self.pos1[0] + 1
            self.pos2[0] = self.pos2[0] + 1

    def tourner(self):
        #on fait tourner le block
        formActuelle = self.formActuelle
        if formActuelle == 3 :
            formActuelle = 0
        else :
            formActuelle = formActuelle + 1
        #on sassure que la forme ne sorte pas de la map
        if self.pos1[0]+len(self.form[formActuelle]) < 23 :
            self.formActuelle = formActuelle
            self.pos2 = [self.pos1[0]+len(self.form[self.formActuelle]),self.pos1[1]+len(self.form[self.formActuelle][0])]
            while self.pos2[1] > 10 :
                self.gauche()

    def getPos1(self):
        return self.pos1

    def getPos2(self):
        return self.pos2

    def getForm(self):
        return self.form
