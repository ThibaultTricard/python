#!/usr/bin/env python
# coding: utf-8
from PodSixNet.Channel import Channel
import pygame
from pygame.locals import *

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
        print(self._server.getNbClient())
        if self._server.getNbClient()<=NB_JOUEUR_LIMITE:
            print('username recu : %s ' % data['username'])
            self.Send({"action":"confirmationConnexion"})
        else:
            self.Send({"action":"connexionRefusee"})

    def Network_message(self,data):
        print data['message']
        for client in self._server.clients:
            if client!=self:
                client.Send({"action":"message","message":data['message']})
    
    def Network_keys(self,data):
        touches = data['keystrokes']
        map=data['map']
       # jeu=data['jeu']
        i=0
        estClientActuelle=True
        for client in self._server.clients:
            if client==self:
                estClientActuelle=False
            if estClientActuelle:
                i=i+1
        if touches[K_LEFT]:
            #current_forme.gauche()
            
           # self.controlerCollision(map,jeu.getForme(i))
            
            for client in self._server.clients:
                    client.Send({"action":"move","message":{"Joueur":i,"Direction":"gauche"}})
            print("left")
        if touches[K_RIGHT]:
            #current_forme.droite()
            for client in self._server.clients:
                    client.Send({"action":"move","message":{"Joueur":i,"Direction":"droite"}})
            print("right")
        if touches[K_DOWN]:
            #current_forme.bas()
            for client in self._server.clients:
                client.Send({"action":"move","message":{"Joueur":i,"Direction":"bas"}})
            print("down")
        if touches[K_SPACE]:
            #current_forme.rotate()
            print("rotate")
            for client in self._server.clients:
                client.Send({"action":"rotate","message":{"Joueur":i}})
    
    def controlerCollision(self,map,forme):
        print("Coucou")
        
