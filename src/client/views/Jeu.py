#!/usr/bin/env python
# coding: utf-8
import pygame
from pygame.locals import *
import sys
sys.path.append('/src/client/controller/JeuController')
from controller.JeuController import JeuController

LARGEUR_FENETRE=int(800)
HAUTEUR_FENETRE=int(600)

class Jeu():

    def __init__(self):
        self.jeuController = JeuController(self)

    def afficherAccueil(self):
        for i in range(0,3):
            for j in range(0,9):
                for k in range (0,)

    def loop(self):
