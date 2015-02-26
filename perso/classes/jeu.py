import sys
import time
from classes import client
from classes import mapLoader
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
        self.carte = mapLoader.create()
        self.carte.draw(self.surface)
        pygame.display.flip()

    def lancer(self):
        monClient = client.Client(self.ip, self.port, self.pseudo, self)
        while True:
            pygame.time.Clock().tick(60)
            monClient.Loop()

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
            keys=pygame.key.get_pressed()
            if keys[K_LEFT] or keys[K_UP] or keys[K_RIGHT] or keys[K_DOWN]:
                monClient.key(keys)
        self.carte.draw(self.surface)
        pygame.display.flip()
