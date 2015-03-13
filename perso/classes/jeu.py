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
    #on prepare le jeu
    def __init__(self, ip, port, pseudo):
        pygame.init()
        self.surface=pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
        self.ip=ip
        self.port=port
        self.pseudo=pseudo
        self.joueurs={0:"pseudo",1:"pseudo",2:"pseudo",3:"pseudo"}
        #formes des joueurs 0,1,2,3
        self.forms = {0:FORM_VIDE,1:FORM_VIDE,2:FORM_VIDE,3:FORM_VIDE}
        #formes qui bougent
        self.groupeForm = {0:pygame.sprite.RenderClear(),1:pygame.sprite.RenderClear(),2:pygame.sprite.RenderClear(),3:pygame.sprite.RenderClear()}
        #formes qui ne bougent pas
        self.groupeFormStockee = {0:pygame.sprite.RenderClear(),1:pygame.sprite.RenderClear(),2:pygame.sprite.RenderClear(),3:pygame.sprite.RenderClear()}
        self.score={'0':0,'1':0,'2':0,'3':0}
        #on laisse la variable begin a False
        self.begin = False
        self.carte = mapLoader.create()
        self.carte.draw(self.surface)
        pygame.display.flip()

    #on lance le jeu
    def lancer(self):
        monClient = client.Client(self.ip, self.port, self.pseudo, self)
        monClient.demanderMap()
        clock = pygame.time.Clock()
        cd = 0
        cdDown = 0
        while True:
            self.surface.fill(pygame.Color("black"))
            clock.tick(60)
            monClient.Loop()
            #on dessine la carte sur le jeu
            self.carte.draw(self.surface)
            #on fait dimminuer les couldown
            if cd > 0 :
                cd = cd -1
            if cdDown > 0 :
                cdDown = cdDown -1
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
            keystrokes = pygame.key.get_pressed()
            #on ne prend pas en compte les input tant que le jeu n'est pas commencé
            if self.begin :
                if keystrokes[K_LEFT] or keystrokes[K_UP] or keystrokes[K_RIGHT]:
                    if cd == 0 :
                        #on envoi le tableau de touche au serveur
                        monClient.keys(keystrokes)
                        cd = 5

                #toutes les 10/60eme de seconde on fait descendre
                if keystrokes[K_DOWN] :
                    monClient.keys(keystrokes)
                    cdDown=10
                if cdDown == 0 :

                    monClient.down()
                    cdDown=10
            #on dessine la carte
            self.carte.draw(self.surface)
            #on dessine les forme
            for g in self.groupeForm :
                self.groupeForm[g].draw(self.surface)
            #on dessine les forme qui son déjà tombé
            for g in self.groupeFormStockee :
                self.groupeFormStockee[g].draw(self.surface)
            #on ecrie les scores
            for i in [0,1,2,3]:
                self.surface.blit(mapLoader.ecrireScore(self.joueurs[i],str(self.score[str(i)])),(50+i*180,30))
            pygame.display.flip()

    #on fait bouger les formes
    def move(self,joueur,direction):
        if direction == "bas" :
            self.forms[joueur].bas()
        if direction == "gauche" :
            self.forms[joueur].gauche()
        if direction == "droite" :
            self.forms[joueur].droite()
        self.groupeForm[joueur] = mapLoader.paint(self.forms[joueur],joueur)

    #on crée un frome pour un joueur
    def create(self,joueur,form):
        self.forms[joueur] = forme.Forme([0,4],[len(form[0]),4+len(form[0][0])],form)
        self.groupeForm[joueur] = mapLoader.paint(self.forms[joueur],joueur)
        self.score[joueur]=0

    #on set le pseudo d'un joueur
    def setPseudoJoueur(self,joueur,pseudo):
        self.joueurs[int(joueur)]=pseudo
        print "pseudo Joueur "+str(self.joueurs[int(joueur)])

    #on fait tourner la forme d'un joueur
    def rotate(self,joueur):
        self.forms[joueur].tourner()
        self.groupeForm[joueur] = mapLoader.paint(self.forms[joueur],joueur)

    #on redessine la carte d'un joueur
    def refresh(self,joueur, MAP) :
        form = forme.Forme([0,0],[21,10],{0:MAP})
        self.groupeFormStockee[joueur] = mapLoader.paint(form,joueur)

    #fonction qui augmente le score d'un joueur
    def augmenterScore(self,joueur,score):
        self.score[str(joueur)]=self.score[str(joueur)]+int(score)
        print "Augmenter joueur "+str(self.score[str(joueur)])
        print "Joueur a augmenter : "+str(joueur)

    #fait débuter la partie
    def commencer(self):
        self.begin = True

    #indique au jeu qu'un joueur a eu une collision et met ses block dans le groupe
    #de block immobile
    def collision(self , joueur):
        for s in self.groupeForm[joueur].sprites():
            self.groupeFormStockee[joueur].add(s)

    def getMap(self):
        return self.MAP

    def getForms(self,joueur):
        return self.forms[joueur]
