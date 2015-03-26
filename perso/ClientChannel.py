#!/usr/bin/env python
# coding: utf-8
from PodSixNet.Channel import Channel
import pygame
from pygame.locals import *
import copy
import random
from classes import dictForme
from classes import forme

NB_JOUEUR_LIMITE=2

#Héritage de la classe Channel
#La classe Channel a un attribut _server
class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)

    def Close(self):
        self._server.del_client(self)

    def Network(self,data):
        print('message de type %s recu' % data['action'])

    #Ajoute le pseudo du client Chanel
    def Network_username(self,data):
        if self._server.getNbClient()<=NB_JOUEUR_LIMITE:
            print('username recu : %s ' % data['username'])
            self._server.ajouterPseudo(data['username'])
        else:
            self.Send({"action":"connexionRefusee"})


    def Network_message(self,data):
        print data['message']
        for client in self._server.clients:
            if client!=self:
                client.Send({"action":"message","message":data['message']})

    #On recupere le joueur actuelle
    def joueurActuelle(self):
        estClientActuelle=True
        i=0
        for client in self._server.clients:
            if client==self:
                estClientActuelle=False
            if estClientActuelle:
                i=i+1
        return i
    #fait descendre la forme d'un joueur
    def actionDown(self,formeActuelle,MAP,joueur):
        #on fait decendre la forme
        formeActuelle.bas()
        #on verifie si il y a une collision
        if self.controlerCollision(MAP,formeActuelle) :
            self._server.forms[joueur] = formeActuelle
            for client in self._server.clients:
                client.Send({"action":"move","message":{"Joueur":joueur,"Direction":"bas"}})
        #si il y a collision ou si la forme touche en bas
        if not self.controlerCollision(MAP,formeActuelle) or self._server.forms[joueur].pos2[0] == 22 :
            #on dit à tous les clients qu'un joueur a posé une forme
            for client in self._server.clients:
                client.Send({"action":"poser","joueur":joueur})
            #on tranfert la forme du joueur vers sa map
            self.collision(joueur)

            #on s'occupe des eventuelles lignes
            self.checkLigne({})

            #on crée une nouvelle forme
            nbForme=random.randint(0,6)
            dict=dictForme.DictForme()
            formes=dict.getFormes()
            self._server.forms[joueur] = forme.Forme([0,4],[len(formes[nbForme][0]),4+len(formes[nbForme][0][0])],formes[nbForme])

            #on controle si il y a une collision entre la nouvelle forme et les blocks
            if (self.controlerCollision(self._server.MAPS[joueur],self._server.forms[joueur])):
                #si il n'y a pas de collision on envoie la forme à tous les clients
                for client in self._server.clients:
                    client.Send({"action":"former","joueur":joueur,"forme":formes[nbForme]})
            else :
                #sinon on signale au client concerné qu'il a perdu
                self._server.joueurActifs[joueur]=0
                if self.finDuJeu():
                    for client in self._server.clients:
                        client.Send({"action":"fin", 'fin':'fin','gagnant':self.gagnant()})
                else:
                    self.Send({"action":"fin", 'fin':'fin','gagnant':""})


    #Gère les touches claviers envoyées
    def Network_keys(self,data):
        touches = data['keystrokes']
        joueur=self.joueurActuelle()
        #on copie la frome du joueur
        formeActuelle = copy.deepcopy(self._server.forms[joueur])
        MAP = copy.deepcopy(self._server.MAPS[joueur])
        #on regarde quelle touche a été appuyée
        if touches[K_LEFT]:
            #on fait bouger la copie de la forme
            formeActuelle.gauche()
            #on controlle les collisions sur la copie
            if self.controlerCollision(MAP,formeActuelle) :
                #si il n'y a pas de collions on reporte l'action effectuée sur la vraie forme
                self._server.forms[joueur] = formeActuelle
                #on informe les clients du mouvement effectué
                for client in self._server.clients:
                    client.Send({"action":"move","message":{"Joueur":joueur,"Direction":"gauche"}})
        if touches[K_RIGHT]:
            #on fait bouger la copie de la forme
            formeActuelle.droite()
            if self.controlerCollision(MAP,formeActuelle) :
                self._server.forms[joueur] = formeActuelle
                for client in self._server.clients:
                    client.Send({"action":"move","message":{"Joueur":joueur,"Direction":"droite"}})
        if touches[K_DOWN]:
            #on fait descendre la forme
            self.actionDown(formeActuelle,MAP,joueur)

        if touches[K_UP]:
            #on fait tourner la piece
            formeActuelle.tourner()
            if self.controlerCollision(MAP,formeActuelle) :
                self._server.forms[joueur] = formeActuelle
                for client in self._server.clients:
                    client.Send({"action":"rotate","message":{"Joueur":joueur}})

    #Methode qui verifie si des lignes ont été faites
    #on parcours les lignes pour trouver les lignes
    #si il y a des ligne on décalle les lignes supérieures vers les bas
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
        #on informe les clients de la nouvelle carte
        for client in self._server.clients:
                client.Send({"action":"refreshMap","message":{"Joueur":joueur,"MAP":MAP}})
                if compteurLigneModifiee!=0:
                    score=self.calculerScore(compteurLigneModifiee)
                    self._server.scores[joueur] = self._server.scores[joueur]+score
                    client.Send({"action":"augmenterScore","Joueur":joueur,"score":score})

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

    #on fait descendre la forme
    def Network_down(self,date):
        joueur=self.joueurActuelle()
        formeActuelle=copy.deepcopy(self._server.forms[joueur])
        MAP = copy.deepcopy(self._server.MAPS[joueur])
        self.actionDown(formeActuelle,MAP,joueur)

    #on verifie les collisions entre la map et le joueur en utilisant une superposition
    def collision(self, joueur):
        for i in range(len(self._server.forms[joueur].form[self._server.forms[joueur].formActuelle])) :
            for j in range(len(self._server.forms[joueur].form[self._server.forms[joueur].formActuelle][i])):
                if  self._server.forms[joueur].form[self._server.forms[joueur].formActuelle][i][j] >= 1 :
                    self._server.MAPS[joueur][i + self._server.forms[joueur].pos1[0] ][j + self._server.forms[joueur].pos1[1]] = self._server.forms[joueur].form[self._server.forms[joueur].formActuelle][i][j]

    #on verifie les collisions entre la map et la forme active en utilisant une superposition
    def controlerCollision(self, MAP,forme) :
        for i in range(len(forme.form[forme.formActuelle])) :
            for j in range(len(forme.form[forme.formActuelle][i])):
                if forme.form[forme.formActuelle][i][j] >=1  :
                    if MAP[i + forme.pos1[0]][j + forme.pos1[1]] >= 1 :
                        return False
        return True

    def getPseudo(self):
        return self.pseudo

    def finDuJeu(self):
        fin=True
        for i in range(0,NB_JOUEUR_LIMITE):
            if self._server.joueurActifs[i]!=0:
                fin=False
        return fin
    def gagnant(self):
        score=-1
        gagant=""
        for i in range(0,NB_JOUEUR_LIMITE):
            if self._server.scores[i]>score:
                score=self._server.scores[i]
                gagnant=self._server.pseudos[i]
        return gagnant
