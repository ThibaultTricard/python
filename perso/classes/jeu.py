import sys
import time
from classes import client
from classes import mapLoader
from classes import forme
from classes import block
import pygame
from pygame.locals import *
from pygame.sprite import groupcollide
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
        #formes des joueurs 0,1,2,3
        self.forms = {0:FORM_VIDE,1:FORM_VIDE,2:FORM_VIDE,3:FORM_VIDE}
        #formes qui bougent
        self.groupeForm = {0:pygame.sprite.RenderClear(),1:pygame.sprite.RenderClear(),2:pygame.sprite.RenderClear(),3:pygame.sprite.RenderClear()}
        #formes qui ne bougent pas
        self.groupeFormStockee = {0:pygame.sprite.RenderClear(),1:pygame.sprite.RenderClear(),2:pygame.sprite.RenderClear(),3:pygame.sprite.RenderClear()}
        self.begin = False
        self.carte = mapLoader.create()
        self.carte.draw(self.surface)
        pygame.display.flip()

    def lancer(self):
        monClient = client.Client(self.ip, self.port, self.pseudo, self)
        monClient.demanderMap()
        clock = pygame.time.Clock()
        #pygame.key.set_repeat(1,1)
        cd = 0
        while True:
            clock.tick(60)
            monClient.Loop()
            if cd > 0 :
                cd = cd -1
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
            keystrokes = pygame.key.get_pressed()
            if self.begin :
                if keystrokes[K_LEFT] or keystrokes[K_SPACE] or keystrokes[K_RIGHT]:
                    if cd == 0 :
                        monClient.keys(keystrokes)
                        cd = 10

                if keystrokes[K_DOWN] :
                    monClient.keys(keystrokes)

            self.carte.draw(self.surface)
            for g in self.groupeForm :
                self.groupeForm[g].draw(self.surface)
            for g in self.groupeFormStockee :
                self.groupeFormStockee[g].draw(self.surface)    
            pygame.display.flip()

    def move(self,joueur,direction):
        if direction == "bas" :
            self.forms[joueur].bas()
        if direction == "gauche" :
            self.forms[joueur].gauche()
        if direction == "droite" :
            self.forms[joueur].droite()
        self.groupeForm[joueur] = mapLoader.paint(self.forms[joueur],joueur)

    def create(self,joueur,form):
        self.forms[joueur] = forme.Forme([0,4],[len(form[0]),4+len(form[0][0])],form)
        self.groupeForm[joueur] = mapLoader.paint(self.forms[joueur],joueur)

    def rotate(self,joueur):
        self.forms[joueur].tourner()
        self.groupeForm[joueur] = mapLoader.paint(self.forms[joueur],joueur)

    def refresh(self,joueur, map) :
        form = forme.Forme([0,0],[21,10],{0:map})
        self.groupeFormStockee[joueur] = mapLoader.paint(form,joueur)

    def commencer(self):
        self.begin = True
                
    def collision(self , joueur):
        for s in self.groupeForm[joueur].sprites():
            self.groupeFormStockee[joueur].add(s)
    
    def getMap(self):
        return self.MAP

    def getForms(self,joueur):
        return self.forms[joueur]
