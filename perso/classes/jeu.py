import sys
import time
from classes import client
from classes import mapLoader
from classes import forme
import pygame
from pygame.locals import *
FORM_VIDE = forme.Forme([0,0],[0,0],{0:{},
             1:{},
             2:{},
             3:{}})
LARGEUR_FENETRE=int(800)
HAUTEUR_FENETRE=int(600)

class Jeu() :
    def __init__(self, ip, port, pseudo):
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        self.ip=ip
        self.port=port
        self.pseudo=pseudo
        self.forms = {0:FORM_VIDE,1:FORM_VIDE,2:FORM_VIDE,3:FORM_VIDE}
        self.groupeForm = {0:pygame.sprite.RenderClear(),1:pygame.sprite.RenderClear(),2:pygame.sprite.RenderClear(),3:pygame.sprite.RenderClear()}
        self.begin = False
        self.carte = mapLoader.create()
        self.carte.draw(self.surface)
        pygame.display.flip()

    def lancer(self):
        monClient = client.Client(self.ip, self.port, self.pseudo, self)
        clock = pygame.time.Clock()
        pygame.key.set_repeat(1,1)
        while True:
            clock.tick(60)
            monClient.Loop()

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
            keystrokes = pygame.key.get_pressed()
            if self.begin :
                if keystrokes[K_LEFT] or keystrokes[K_SPACE] or keystrokes[K_RIGHT] or keystrokes[K_DOWN]:
                    monClient.keys(keystrokes)
        self.carte.draw(self.surface)
        pygame.display.flip()

    def move(self,joueur,direction):
        pass

    def create(self,joueur,form):
        pass

    def rotate(self,joueur):
        pass

    def refresh(self,joueur, map) :
        pass

    def commencer(self):
        self.begin = True
