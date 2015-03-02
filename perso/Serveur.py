#!/usr/bin/env python
# coding: utf-8
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from ClientChannel import ClientChannel
from classes import dictForme
import time
import random

#Héritage de la classe Server
class MyServer(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.clients = []
        print('Server launched')

    def Connected(self, channel, addr):
        print('New connection')
        self.clients.append(channel)

    def del_client(self,channel):
        print('client deconnecte')
        self.clients.remove(channel)


    def launch_game(self):
        # Init Pygame
        print("game launched")
        nbFormeJ1=random.randint(0,6)
        nbFormeJ2=random.randint(0,6)
        nbFormeJ3=random.randint(0,6)
        nbFormeJ4=random.randint(0,6)
        dict=dictForme.DictForme()
        formes=dict.getFormes()
        for client in self.clients:
            client.Send({"action":"former","joueur":1,"forme":formes[nbFormeJ1]})
            client.Send({"action":"former","joueur":2,"forme":formes[nbFormeJ2]})
            client.Send({"action":"former","joueur":3,"forme":formes[nbFormeJ3]})
            client.Send({"action":"former","joueur":4,"forme":formes[nbFormeJ4]})
        while True:
            time.sleep(0.01)
            self.Pump()



class ClientChannel(Channel):

    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)
        self.current_forme=pygame.Sprite.RenderClear()

    def Close(self):
        self._server.del_client(self)
