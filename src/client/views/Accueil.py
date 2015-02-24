#!/usr/bin/env python
# coding: utf-8
import pygame
from pygame.locals import *
import threading
import sys
from pygame import Surface
sys.path.append('/src/client/controller/AccueilController')
from src.client.controller.AccueilController import AccueilController

LARGEUR_FENETRE=int(800)
HAUTEUR_FENETRE=int(600)
CHEMIN_BACKGROUND="../../image/tetris.jpg"

class Accueil():
    def __init__(self):
       # self.surface=Surface((LONGUEUR_FENETRE,LARGEUR_FENETRE))
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        self.setBackground(CHEMIN_BACKGROUND)
        self.afficherBackground()
        pygame.display.flip()
        threading.Thread(target=self.loop()).start()
        self.accueilController=AccueilController
        
    def loop(self):
        while 1:
            self.afficherBackground()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==MOUSEBUTTONDOWN:
                    pass
                if event.type == QUIT:     
                    sys.exit(0)
                    
    def setBackground(self,backgroundImage):
        self.background=pygame.image.load(backgroundImage).convert()
        
    def afficherBackground(self):
        self.surface.blit(self.background,(0,0))
        
    def creerBoutonJouer(self,boutonJouer):
        #Créer bouton jouer
        self.boutonJouer=boutonJouer
    def creerBoutonQuitter(self,boutonQuitter):
        self.boutonQuitter=boutonQuitter
        
    def getSurface(self):
        return self.surface
    