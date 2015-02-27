#!/usr/bin/env python
# coding: utf-8
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from ClientChannel import ClientChannel

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

class ClientChannel(Channel):

    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)
        self.current_forme=pygame.Sprite.RenderClear()

    def Close(self):
        self._server.del_client(self)

    def Network_keys(self,data):
        touches = data['keystrokes']
        if(touches[K_LEFT]):
            current_forme.gauche()
        if(touches[K_RIGHT]):
            current_forme.droite()
        if(touches[K_DOWN]):
            current_forme.bas()
        if(touches[K_SPACE]):
            current_forme.rotate()
