#!/usr/bin/env python
# coding: utf-8
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from ClientChannel import ClientChannel
from classes import dictForme
from classes import map
from classes import forme
import time
import random
import copy
FORM_VIDE = forme.Forme([0,0],[0,0],{0:{},
             1:{},
             2:{},
             3:{}})

#Héritage de la classe Server
class MyServer(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.clients = []
        self.MAPS= {0:copy.deepcopy(map.MAP),1:copy.deepcopy(map.MAP),2:copy.deepcopy(map.MAP),3:copy.deepcopy(map.MAP)}
        self.forms={0:FORM_VIDE,1:FORM_VIDE,2:FORM_VIDE,3:FORM_VIDE}
        print('Server launched')

    def Connected(self, channel, addr):
        print('New connection')
        self.clients.append(channel)

    def del_client(self,channel):
        print('client deconnecte')
        self.clients.remove(channel)

    def getNbClient(self):
        return len(self.clients)

    def getMapParJoueur(self,joueur):
        return self.MAPS[joueur]

    def launch_game(self):
        # Init Pygame
        print("game launched")
        nbFormeJ0=random.randint(0,6)
        nbFormeJ1=random.randint(0,6)
        nbFormeJ2=random.randint(0,6)
        nbFormeJ3=random.randint(0,6)
        dict=dictForme.DictForme()
        formes=dict.getFormes()
        for client in self.clients:
            client.Send({"action":"former","joueur":0,"forme":formes[nbFormeJ0]})
            client.Send({"action":"former","joueur":1,"forme":formes[nbFormeJ1]})
            client.Send({"action":"former","joueur":2,"forme":formes[nbFormeJ2]})
            client.Send({"action":"former","joueur":3,"forme":formes[nbFormeJ3]})
        self.forms={0:forme.Forme([0,4],[len(formes[nbFormeJ0][0]),4+len(formes[nbFormeJ0][0][0])],formes[nbFormeJ0])
                    ,1:forme.Forme([0,4],[len(formes[nbFormeJ1][0]),4+len(formes[nbFormeJ1][0][0])],formes[nbFormeJ1])
                    ,2:forme.Forme([0,4],[len(formes[nbFormeJ2][0]),4+len(formes[nbFormeJ2][0][0])],formes[nbFormeJ2])
                    ,3:forme.Forme([0,4],[len(formes[nbFormeJ3][0]),4+len(formes[nbFormeJ3][0][0])],formes[nbFormeJ3])}
        print self.forms[0]
        while True:
            time.sleep(0.01)
            self.Pump()
