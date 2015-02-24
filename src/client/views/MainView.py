#!/usr/bin/env python
# coding: utf-8
import pygame
import os
from pygame.locals import *
import sys
import imp
sys.path.append('/src/client/views/LoadImage')
from LoadImage import LoadImage

LARGEUR_FENETRE=800
LONGUEUR_FENETRE=600
class MainView(pygame.display):
    def __init__(self):
        pygame.init()
        self.image=""
        
    def setBackground(self,cheminBackgroundImage):
        self.image = cheminBackgroundImage
        print self.image
        
    def afficherFenetre(self):
        fenetre=pygame.display.set_mode((LARGEUR_FENETRE,LONGUEUR_FENETRE))
        self.image = pygame.image.load(self.image).convert()
        fenetre.blit(self.image, (0,0))
        pygame.display.flip()
        while 1:
            for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    sys.exit(0)  
            fenetre.blit(self.image, (0,0))
            pygame.display.flip()       
    
   
    
    