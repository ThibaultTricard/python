#!/usr/bin/env python
# coding: utf-8
from PodSixNet.Channel import Channel
import pygame
from pygame.locals import *
import copy
import random
from classes import dictForme
from classes import forme

Block_Ligne = {0 : { 0 : [1],
                     1 : [1],
                     2 : [1],
                     3 : [1]},
               1 : { 0 : [1,1,1,1]},
               2 : { 0 : [1],
                     1 : [1],
                     2 : [1],
                     3 : [1]},
               3 : {0 : [1,1,1,1]}}

Block_Tee =   {0 : { 0 : [0,2,0],
                     1 : [2,2,2]},
               1 : { 0 : [0,2],
                     1 : [2,2],
                     2 : [0,2]},
               2 : { 0 : [2,2,2],
                     1 : [0,2,0]},
               3 : { 0 : [2,0],
                     1 : [2,2],
                     2 : [2,0]}}

Block_S1 =    {0 : {0 : [3,3,0],
                    1 : [0,3,3]},
               1 : {0 : [0,3],
                    1 : [3,3],
                    2 : [3,0]},
               2 : {0 : [3,3,0],
                    1 : [0,3,3]},
               3 : {0 : [0,3],
                    1 : [3,3],
                    2 : [3,0]}}

Block_S2 =      {0 : {0 : [0,4,4],
                      1 : [4,4,0]},
                 1 : {0 : [4,0],
                      1 : [4,4],
                      2 : [0,4]},
                 2 : {0 : [0,4,4],
                      1 : [4,4,0]},
                 3 : {0 : [4,0],
                      1 : [4,4],
                      2 : [0,4]}}

Block_Cube =   {0 : {0 : [5,5],
                     1 : [5,5]},
                1 : {0 : [5,5],
                     1 : [5,5]},
                2 : {0 : [5,5],
                     1 : [5,5]},
                3 : {0 : [5,5],
                     1 : [5,5]}}

Block_L1=      { 0 : {0 : [6,6],
                      1 : [0,6],
                      2 : [0,6]},
                 1 : {0 : [6,6,6],
                      1 : [6,0,0]},
                 2 : {0 : [0,6],
                      1 : [0,6],
                      2 : [6,6]},
                 3 : {0 : [0,0,6],
                      1 : [6,6,6]}}

Block_L2=      { 0 : {0 : [7,7],
                      1 : [7,0],
                      2 : [7,0]},
                 1 : {0 : [7,0,0],
                      1 : [7,7,7]},
                 2 : {0 : [0,7],
                      1 : [0,7],
                      2 : [7,7]},
                 3 : {0 : [7,7,7],
                      1 : [0,0,7]}}
NB_JOUEUR_LIMITE=4

#Héritage de la classe Channel
#La classe Channel a un attribut _server
class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)

    def Close(self):
        self._server.del_client(self)

    def Network(self,data):
        print('message de type %s recu' % data['action'])

    def Network_username(self,data):
        if self._server.getNbClient()<=NB_JOUEUR_LIMITE:
            print('username recu : %s ' % data['username'])
            self._server.ajouterPseudo(data['username'])
        else:
            self.Send({"action":"connexionRefusee"})

    def Network_rafraichir(self,data):
        i=0
        #for client in self._server.clients:
            #client.Send({"action":"rafraichir","map":self.map,"joueur":i})

    def Network_message(self,data):
        print data['message']
        for client in self._server.clients:
            if client!=self:
                client.Send({"action":"message","message":data['message']})

    def joueurActuelle(self):
        estClientActuelle=True
        i=0
        for client in self._server.clients:
            if client==self:
                estClientActuelle=False
            if estClientActuelle:
                i=i+1
        return i

    def actionDown(self,formeActuelle,MAP,joueur):
        formeActuelle.bas()
        if self.controlerCollision(MAP,formeActuelle) :
            self._server.forms[joueur] = formeActuelle
            for client in self._server.clients:
                client.Send({"action":"move","message":{"Joueur":joueur,"Direction":"bas"}})
            print("down")
        if not self.controlerCollision(MAP,formeActuelle) or self._server.forms[joueur].pos2[0] == 22 :
            for client in self._server.clients:
                client.Send({"action":"poser","joueur":joueur})
            self.collision(joueur)
            self.checkLigne({})
            nbForme=random.randint(0,6)
            dict=dictForme.DictForme()
            formes=dict.getFormes()
            self._server.forms[joueur] = forme.Forme([0,4],[len(formes[nbForme][0]),4+len(formes[nbForme][0][0])],formes[nbForme])
            if (self.controlerCollision(self._server.MAPS[joueur],self._server.forms[joueur])):
                for client in self._server.clients:
                    client.Send({"action":"former","joueur":joueur,"forme":formes[nbForme]})
            else :
                client.send({"action":"fin"})


    def Network_keys(self,data):
        touches = data['keystrokes']
        # jeu=data['jeu']
        joueur=self.joueurActuelle()
        formeActuelle = copy.deepcopy(self._server.forms[joueur])
        MAP = copy.deepcopy(self._server.MAPS[joueur])
        print str(formeActuelle.pos1)
        if touches[K_LEFT]:
            #current_forme.gauche()
            formeActuelle.gauche()
            if self.controlerCollision(MAP,formeActuelle) :
                self._server.forms[joueur] = formeActuelle
                for client in self._server.clients:
                    client.Send({"action":"move","message":{"Joueur":joueur,"Direction":"gauche"}})
                print("left")
        if touches[K_RIGHT]:
            formeActuelle.droite()
            if self.controlerCollision(MAP,formeActuelle) :
                self._server.forms[joueur] = formeActuelle
                for client in self._server.clients:
                    client.Send({"action":"move","message":{"Joueur":joueur,"Direction":"droite"}})
                print("right")
        if touches[K_DOWN]:
            self.actionDown(formeActuelle,MAP,joueur)

        if touches[K_UP]:
            formeActuelle.tourner()
            if self.controlerCollision(MAP,formeActuelle) :
                self._server.forms[joueur] = formeActuelle
                for client in self._server.clients:
                    client.Send({"action":"rotate","message":{"Joueur":joueur}})
                print("rotate")


    def checkLigne(self,data):
        joueur=self.joueurActuelle()
        MAP = self._server.getMapParJoueur(joueur);
        ligneModifie=1
        compteurLigneModifiee=0
        while ligneModifie!=0:
            ligneModifie=0
            for i in range(len(MAP)):
                caseVide=False
                for j in range(len(MAP[i])):
                    if MAP[i][j]==0:
                        caseVide=True
                if caseVide==False:
                    ligneModifie=1
                    compteurLigneModifiee=compteurLigneModifiee+1
                    for k in range(i,1,-1):
                        MAP[k]=MAP[k-1]
        for client in self._server.clients:
                client.Send({"action":"refreshMap","message":{"Joueur":joueur,"MAP":MAP}})
                if compteurLigneModifiee!=0:
                    client.Send({"action":"augmenterScore","Joueur":joueur,"score":self.calculerScore(compteurLigneModifiee)})

    """
    Retourne le score à ajouter au joueur lors de la suppression d'une ligne
    """
    def calculerScore(self,nbLigne):
        if nbLigne==1:
            return 40
        if nbLigne==2:
            return 100
        if nbLigne==3:
            return 300
        if nbLigne==4:
            return 1200

    def Network_down(self,date):
        joueur=self.joueurActuelle()
        formeActuelle=copy.deepcopy(self._server.forms[joueur])
        MAP = copy.deepcopy(self._server.MAPS[joueur])
        self.actionDown(formeActuelle,MAP,joueur)


    def Network_miseAJourMap(self,data):
        #self.map=data["map"]
        pass

    def collision(self, joueur):
        for i in range(len(self._server.forms[joueur].form[self._server.forms[joueur].formActuelle])) :
            for j in range(len(self._server.forms[joueur].form[self._server.forms[joueur].formActuelle][i])):
                if  self._server.forms[joueur].form[self._server.forms[joueur].formActuelle][i][j] >= 1 :
                    self._server.MAPS[joueur][i + self._server.forms[joueur].pos1[0] ][j + self._server.forms[joueur].pos1[1]] = self._server.forms[joueur].form[self._server.forms[joueur].formActuelle][i][j]

    def controlerCollision(self, MAP,forme) :
        for i in range(len(forme.form[forme.formActuelle])) :
            for j in range(len(forme.form[forme.formActuelle][i])):
                if forme.form[forme.formActuelle][i][j] >=1  :
                    if MAP[i + forme.pos1[0]][j + forme.pos1[1]] >= 1 :
                        print "false"
                        return False
        return True
    
    def getPseudo(self):
        return self.pseudo
