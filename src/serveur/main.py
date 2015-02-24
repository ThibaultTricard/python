import sys
import os
import time
import imp
forme = imp.load_source('Forme', '../classes/forme.py')
joueur = imp.load_source('Joueur', '../classes/joueur.py')
carte = imp.load_source('Carte', '../classes/carte.py')
import random
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
import time,sys

MAP =  {0 :[0,0,0,0,0,0,0,0,0,0],
        1 :[0,0,0,0,0,0,0,0,0,0],
        2 :[0,0,0,0,0,0,0,0,0,0],
        3 :[0,0,0,0,0,0,0,0,0,0],
        4 :[0,0,0,0,0,0,0,0,0,0],
        5 :[0,0,0,0,0,0,0,0,0,0],
        6 :[0,0,0,0,0,0,0,0,0,0],
        7 :[0,0,0,0,0,0,0,0,0,0],
        8 :[0,0,0,0,0,0,0,0,0,0],
        9 :[0,0,0,0,0,0,0,0,0,0],
        10:[0,0,0,0,0,0,0,0,0,0],
        11:[0,0,0,0,0,0,0,0,0,0],
        12:[0,0,0,0,0,0,0,0,0,0],
        13:[0,0,0,0,0,0,0,0,0,0],
        14:[0,0,0,0,0,0,0,0,0,0],
        15:[0,0,0,0,0,0,0,0,0,0],
        16:[0,0,0,0,0,0,0,0,0,0],
        17:[0,0,0,0,0,0,0,0,0,0],
        18:[0,0,0,0,0,0,0,0,0,0],
        19:[0,0,0,0,0,0,0,0,0,0],
        20:[0,0,0,0,0,0,0,0,0,0],
        21:[0,0,0,0,0,0,0,0,0,0]}

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

Block_Tee =   {0 : { 0 : [-1, 2,-1],
                     1 : [ 2, 2, 2]},

               1 : { 0 : [-1,2],
                     1 : [ 2, 2],
                     2 : [-1, 2]},

               2 : { 0 : [ 2, 2, 2],
                     1 : [-1, 2,-1]},

               3 : { 0 : [ 2,-1],
                     1 : [ 2, 2],
                     2 : [ 2,-1]}}

Block_S1 =    {0 : {0 : [ 3, 3,-1],
                    1 : [-1, 3, 3]},

               1 : {0 : [-1, 3],
                    1 : [ 3, 3],
                    2 : [ 3,-1]},

               2 : {0 : [ 3, 3,-1],
                    1 : [-1, 3, 3]},

               3 : {0 : [-1, 3],
                    1 : [ 3, 3],
                    2 : [ 3,-1]}}

Block_S2 =      {0 : {0 : [-1, 4, 4],
                      1 : [ 4, 4,-1]},

                 1 : {0 : [ 4,-1],
                      1 : [ 4, 4],
                      2 : [-1, 4]},

                 2 : {0 : [-1, 4, 4],
                      1 : [ 4, 4,-1]},

                 3 : {0 : [ 4,-1],
                      1 : [ 4, 4],
                      2 : [-1, 4]}}

Block_Cube =   {0 : {0 : [5,5],
                     1 : [5,5]},

                1 : {0 : [5,5],
                     1 : [5,5]},

                2 : {0 : [5,5],
                     1 : [5,5]},

                3 : {0 : [5,5],
                     1 : [5,5]}}

Block_L1=      { 0 : {0 : [ 6,6],
                      1 : [-1,6],
                      2 : [-1,6]},

                 1 : {0 : [ 6, 6, 6],
                      1 : [ 6,-1,-1]},

                 2 : {0 : [-1,6],
                      1 : [-1,6],
                      2 : [ 6,6]},

                 3 : {0 : [-1,-1,6],
                      1 : [ 6, 6,6]}}

Block_L2=      { 0 : {0 : [ 7, 7],
                      1 : [ 7,-1],
                      2 : [ 7,-1]},

                 1 : {0 : [ 7,-1,-1],
                      1 : [ 7, 7, 7]},

                 2 : {0 : [-1, 7],
                      1 : [-1, 7],
                      2 : [ 7, 7]},

                 3 : {0 : [ 7, 7, 7],
                      1 : [-1,-1, 7]}}
class ClientChannel(Channel):

    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)
        self.joueur = joueur.Joueur

    def Close(self):
        self._server.del_client(self)

    def Network_keys(self,data):
        touches = data['keystrokes']
        if(touches[K_LEFT]):
            pass
        if(touches[K_RIGHT]):
            pass
        if(touches[K_UP]):
            pass
        if(touches[K_DOWN]):
            pass

    def update():
        sefl.send({"""todo"""});

class MyServer(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.clients = []
        self.run = False
        print('Server launched')

    def Connected(self, channel, addr):
        self.clients.append(channel)
        channel.number = len(self.clients)
        print('New connection: %d client(s) connected' % len(self.clients))
        if len(self.clients) == 1:
            self.run = True

    def update_all(self):
        for client in self.clients:
            client.update()
