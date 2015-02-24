#!/usr/bin/env python
# coding: utf-8
import pygame
from pygame.locals import *
import sys
sys.path.append('/src/client/controller/AccueilController')
from controller.AccueilController import AccueilController  # @UnresolvedImport

LARGEUR_FENETRE=int(800)
HAUTEUR_FENETRE=int(600)
CHEMIN_BACKGROUND="../../image/tetris.jpg"
CHEMIN_NOUVELLE_PARTIE="../../image/NouvellePartie.png"
CHEMIN_BOUTON_QUITTER="../../image/Quitter.png"
POSITION_NOUVELLE_PARTIE=(282,367)
POSITION_QUITTER=(285,417)

class Accueil():
    def __init__(self):
        #AccueilController permet de gérer l'action qui suivra l'appui des touches
        self.accueilController=AccueilController(self)
        
    
    def afficherAccueil(self):
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        #chargement du background
        self.setBackground(CHEMIN_BACKGROUND)
        #chargement bouton nouvelle partie
        self.creerBoutonNouvellePartie(CHEMIN_NOUVELLE_PARTIE)
        #chargement bouton quitter
        self.creerBoutonQuitter(CHEMIN_BOUTON_QUITTER)
        
        #affichage des objets
        self.afficherObjet(self.background,self.boutonNouvellePartie,POSITION_NOUVELLE_PARTIE)
        self.afficherObjet(self.background,self.boutonQuitter,POSITION_QUITTER)
        self.afficherObjet(self.surface,self.background,(0,0))
        
        #Booléen nécessaire pour arrêter la boucle loop()
        self.changementPage=False
        
        #Mise à jour de l'affichage
        pygame.display.flip()
        self.loop()
        
    def loop(self):
        while self.changementPage==False:
            pygame.time.Clock().tick(60)
            
            #affichage des objets
            self.afficherObjet(self.surface,self.background,(0,0))
            self.afficherObjet(self.background,self.boutonNouvellePartie,POSITION_NOUVELLE_PARTIE)
            self.afficherObjet(self.background,self.boutonQuitter,POSITION_QUITTER)
            
            #mise à jour de l'affichage
            pygame.display.flip()
            
            #gestion des évènements
            for event in pygame.event.get():
                if event.type==MOUSEBUTTONDOWN:
                    #le controller récupère les coordonnées de la souris au moment du click
                    self.accueilController.setMouseX(event.pos[0])
                    self.accueilController.setMouseY(event.pos[1])
                    
                    #permet de faire une action en fonction du click
                    self.accueilController.controlerClick()
                if event.type == QUIT:     
                    sys.exit(0)        
                           
    def setBackground(self,backgroundImage):
        self.background=pygame.image.load(backgroundImage).convert()
    
    def afficherObjet(self,surface,objet,(x,y)):
        return surface.blit(objet,(x,y))
        
    def creerBoutonNouvellePartie(self,boutonJouer):
        self.boutonNouvellePartie=pygame.image.load(boutonJouer).convert_alpha()
                    
    def creerBoutonQuitter(self,boutonQuitter):
        self.boutonQuitter=pygame.image.load(boutonQuitter).convert_alpha()
        
    def getSurface(self):
        return self.surface
    
    def getRectBoutonNouvellePartie(self):
        return self.afficherObjet(self.background,self.boutonNouvellePartie,POSITION_NOUVELLE_PARTIE)
    
    def getRectBoutonQuitter(self):
        return self.afficherObjet(self.background,self.boutonQuitter,POSITION_QUITTER)
    
    def getAccueilController(self):
        return self.accueilController
    
    def desinitAccueil(self):
        self.changementPage=True
    
        
    