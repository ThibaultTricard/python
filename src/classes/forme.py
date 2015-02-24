class Forme():

    def __init__(self, pos1, pos2, form):
        self.pos1 = pos1
        self.pos2 = pos2
        self.form = form

    def gauche(self):
        if (self.pos1[0] > 0):
            self.pos1[0] = self.pos1[0] - 1
            self.pos2[0] = self.pos2[0] - 1

    def droite(self):
        if (self.pos1[0] < 10):
            self.pos1[0] = self.pos1[0] + 1
            self.pos2[0] = self.pos2[0] + 1

    def bas(self):
        self.pos1[1] = self.pos1[1] + 1
        self.pos2[1] = self.pos2[1] + 1
