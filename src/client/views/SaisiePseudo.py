#!/usr/bin/env python
# coding: utf-8
import pygame
from pygame.locals import *
import imp
import sys
eztext = imp.load_source('eztext', '../classes/eztext.py')

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
    def __init__(self,client):
        self.saisiePseudoController=SaisiePseudoController(self)
        self.client=client

    def afficherSaisiePseudo(self):
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        self.setBackground(CHEMIN_BACKGROUND)
        self.changementPage=False
        self.afficherObjet(self.surface,self.background,(0,0))
        """"""
        self.inputNom = eztext.Input(maxlength=45, color=(0,0,0), prompt='Entrez votre pseudo : ')
        """"""
        pygame.display.flip()
        self.loop()

    def loop(self):
        while self.changementPage==False:
            pygame.time.Clock().tick(60)
            self.afficherObjet(self.surface,self.background,(0,0))
            events = pygame.event.get()
            for event in events :
                if event.type==MOUSEBUTTONDOWN:
                    print "Click"
                if event.type == QUIT:
                    sys.exit(0)
            keys=pygame.key.get_pressed()
            if keys[K_RETURN]:
                self.saisiePseudoController.envoyerPseudo(self.inputNom.value)
                self.changementPage=True
            self.inputNom.update(events)
            self.inputNom.draw(self.surface)
            pygame.display.flip()


    def setBackground(self,backgroundImage):
        self.background=pygame.image.load(backgroundImage).convert()

    def afficherObjet(self,surface,objet,(x,y)):
        return surface.blit(objet,(x,y))
