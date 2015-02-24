#!/usr/bin/env python
# coding: utf-8
import pygame
import os
from pygame.locals import *
import sys
import imp
sys.path.append('/src/client/views/LoadImage')
from LoadImage import LoadImage
from Accueil import Accueil

LARGEUR_FENETRE=800
LONGUEUR_FENETRE=600
class MainView():
    def __init__(self):
        pygame.init()
    
    def setFenetre(self,fenetre):
        self.fenetre=fenetre
        
        
        
       # while 1:
           # for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
             #   if event.type == QUIT:     #Si un de ces événements est de type QUIT
              #      sys.exit(0)
                    
            #self.fenetre.blit()
            #pygame.display.flip()       
    
   
    
    