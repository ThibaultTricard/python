#!/usr/bin/env python
# coding: utf-8
import pygame

class Accueil(pygame.display):
    def __init__(self):
        self.background=""
        self.boutonJouer=""
        self.boutonQuitter=""
    
    def setBackground(self,backgroundImage):
        self.backgroundImage=backgroundImage
    
    def creerBoutonJouer(self,boutonJouer):
        #Créer bouton jouer
        self.boutonJouer=boutonJouer
    def creerBoutonQuitter(self,boutonQuitter):
        self.boutonQuitter=boutonQuitter