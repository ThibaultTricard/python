import pygame
from pygame.locals import *
import sys
sys.path.append('/src/client/controller/AttenteController')
from controller.AttenteController import AttenteController
class Attente():
    def __init__(self):
        self.AttenteController=AttenteController(self)

    def afficherSaisiePseudo(self):
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        self.changementPage=False
        pygame.display.flip()
        chaine="ma chaine sur une seule ligne"
        font=pygame.font.SysFont("broadway",24,bold=False,italic=False)
        text=font.render(chaine,1,(R,G,B))
        surface.blit(text,(30,30))
        surface.display.flip()
        self.loop()

    def loop(self):
        while self.changementPage==False:
            pass

    def changementPage(self):
        self.changementPage=True
