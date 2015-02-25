import sys

class AccueilController:
    def __init__(self,accueil):
        #recuperation de la classe accueil pour pouvoir recuperer les positions des boutons...
        self.accueil=accueil

    def setClient(self,client):
        self.client=client

    def getClient(self):
        return self.client

    def setMouseX(self,X):
        self.mouseX=X

    def setMouseY(self,Y):
        self.mouseY=Y

    """
    Permet de tester si le bouton passe en parametre a ete clique
    """
    def estCliqueBouton(self,bouton):
        if bouton.collidepoint((self.mouseX,self.mouseY))==True:
            return True
        return False

    """
    Si Nouvelle partie faire nouvelle partie
    Si quitter on quitte le programme
    """
    def controlerClick(self):
        if self.estCliqueBouton(self.accueil.getRectBoutonNouvellePartie())==True:
            self.nouvellePartie()
        if self.estCliqueBouton(self.accueil.getRectBoutonQuitter())==True:
            self.quitter()

    """
    Lance une nouvelle partie, le client demande au serveur une nouvelle partie
    """
    def nouvellePartie(self):
        self.accueil.desinitAccueil()
        self.client.demanderNouvellePartie()

    def quitter(self):
        sys.exit(0)
