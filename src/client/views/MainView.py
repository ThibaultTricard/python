#!/usr/bin/env python
# coding: utf-8
import pygame
import os
from pygame.locals import *
import sys
import imp
sys.path.append('/src/client/views/LoadImage')
from Accueil import Accueil

"""
Cette classe est une fenetre de base. Le contenu est mis
quand on fait appel à setFenetre()
"""
class MainView():
    def __init__(self):
        pygame.init()

    """
    Permet de changer le contenu de la fenetre principale
    """
    def setFenetre(self,fenetre):
        self.fenetre=fenetre
    
    def getFenetre(self):
        return self.fenetre    
    """
    Vire la fenetre courante afin d'être remplacée par une autre par la suite
    """
    def desinitFenetre(self):
        self.fenetre=None  
    
   
    
    