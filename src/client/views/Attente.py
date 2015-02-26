import pygame
from pygame.locals import *
import sys
sys.path.append('/src/client/controller/AttenteController')
from controller.AttenteController import AttenteController  # @UnresolvedImport

LARGEUR_FENETRE=int(800)
HAUTEUR_FENETRE=int(600)

class Attente():
    def __init__(self):
        self.attenteController=AttenteController(self)

    def ecranAttente(self):
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        self.changementPage=False
        pygame.display.flip()
        chaine="en attente d'autres joueur"
        font=pygame.font.SysFont("broadway",24,bold=False,italic=False)
        self.text=font.render(chaine,1,(255,255,255))
        self.surface.blit(self.text,(30,30))
        pygame.display.flip()
        self.loop()

    def loop(self):
        while self.changementPage==False:
            pygame.time.Clock().tick(60)
            self.surface.blit(self.text,(30,30))
            pygame.display.flip()


    def changementPage(self):
        self.changementPage=True
