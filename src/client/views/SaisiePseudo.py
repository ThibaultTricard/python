#!/usr/bin/env python
# coding: utf-8
import pygame
from pygame.locals import *
import sys

sys.path.append('/src/client/controller/SaisiePseudoController')
from controller.SaisiePseudoController import SaisiePseudoController # @UnresolvedImport
LARGEUR_FENETRE=800
HAUTEUR_FENETRE=600
CHEMIN_BACKGROUND="../../image/tetris.jpg"

"""
A Continuer seul le background a été mis pour tester que l'affichage fonctionnerait
Cordialement,
DJ Chedriche
"""
class SaisiePseudo:
    def __init__(self):
        self.saisiePseudoController=SaisiePseudoController(self)
    
    def afficherSaisiePseudo(self):
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        self.setBackground(CHEMIN_BACKGROUND)
        self.changementPage=False
        self.afficherObjet(self.surface,self.background,(0,0))
        
        pygame.display.flip()
        self.loop()
        
    def loop(self):
        while self.changementPage==False:
            pygame.time.Clock().tick(60)
            self.afficherObjet(self.surface,self.background,(0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==MOUSEBUTTONDOWN:
                    print "Click"
                if event.type == QUIT:     
                    sys.exit(0)   
        
        
    def setBackground(self,backgroundImage):
        self.background=pygame.image.load(backgroundImage).convert()
        
    def afficherObjet(self,surface,objet,(x,y)):
        return surface.blit(objet,(x,y))
        