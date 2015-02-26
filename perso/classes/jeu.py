import sys
import time
from classes import client
import pygame
from pygame.locals import *

LARGEUR_FENETRE=int(800)
HAUTEUR_FENETRE=int(600)

class Jeu() :
    def __init__(self, ip, port, pseudo):
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        self.ip=ip
        self.port=port
        self.pseudo=pseudo


    def lancer(self):
        monClient = client.Client(self.ip, self.port, self.pseudo)
        while True:
            pygame.time.Clock().tick(60)
            monClient.Loop()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
