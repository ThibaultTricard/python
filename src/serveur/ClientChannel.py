#!/usr/bin/env python
# coding: utf-8
from PodSixNet.Channel import Channel


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
        print('username reçu : %s ' % data['username'])

    def Network_message(self,data):
        print data['message']
        for client in self._server.clients:
            if client!=self:
                client.Send({"action":"message","message":data['message']})
    
    """
    suite à la demande de connexion du client, le serveur confirme la connexion
    Il y'a des tests à faire mais là jsuis fatigué il est minuit 53
    """
    def Network_demandeConnexion(self,data):
        self.Send({"action":"confirmationConnexion"})
        