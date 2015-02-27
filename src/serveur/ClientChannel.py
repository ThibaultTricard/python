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
        print('username recu : %s ' % data['username'])

    def Network_message(self,data):
        print data['message']
        for client in self._server.clients:
            if client!=self:
                client.Send({"action":"message","message":data['message']})

    def Network_keys(self,data):
        touches = data['keystrokes']
        if touches[K_LEFT]:
            #current_forme.gauche()
            print("left")
        if touches[K_RIGHT]:
            #current_forme.droite()
            print("right")
        if touches[K_DOWN]:
            #current_forme.bas()
            print("down")
        if touches[K_SPACE]:
            #current_forme.rotate()
            print("rotate")

    """
    suite à la demande de connexion du client, le serveur confirme la connexion
    Il y'a des tests à faire mais là jsuis fatigué il est minuit 53
    """
    def Network_demandeConnexion(self,data):
        self.Send({"action":"confirmationConnexion"})
