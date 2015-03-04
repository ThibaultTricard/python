#!/usr/bin/env python
# coding: utf-8

import sys
from PodSixNet.Connection import connection, ConnectionListener
import thread
# This example uses Python threads to manage async input from sys.stdin.
# This is so that I can receive input from the console whilst running the server.
# Don't ever do this - it's slow and ugly. (I'm doing it for simplicity's sake)

class bcolors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Client(ConnectionListener):
    def __init__(self, host, port, pseudo, jeu):
        self.Connect((host, port))
        self.pseudo = pseudo
        self.jeu=jeu
        t=thread.start_new_thread(self.Input_loop,())

    def Loop(self):
        connection.Pump()
        self.Pump()

    def Network(self, data):
        print('message de type %s recu' % data['action'])

    ### Network event/message callbacks ###
    def Network_connected(self, data):
        print('connecte au serveur !')
        connection.Send({"action":"username","username":self.pseudo})

    def Network_message(self,data):
        print(data['message'])

    def Network_error(self, data):
        print 'error:', data['error'][1]
        connection.Close()
        
    def Network_connexionRefusee(self,data):
        print "Desole plus de place !"
        sys.exit()
        
    def Network_former(self,data):
        print "former"
        print str(data)
        self.jeu.create(data["joueur"],data["forme"])

    def Network_poser(self,data):
        print "poser"
        self.jeu.collision(data["joueur"])

    def Network_rafraichir(self,data):
        print 'rafraichir'
        self.jeu.refresh(data["joueur"],data["map"])
    
    def Network_deconnexion(self,data):
        print "deconnexion"
        connection.close()
        sys.exit()
        
    def demanderNouvellePartie(self):
        print "Demande nouvelle partie"
        connection.Send({"action":"demandeConnexion"})

    def Network_ready(self,data):
        self.jeu.commencer()

    def Input_loop(self):
        while True:
            #envoyer les commandes saisies
            message=raw_input(">")
            connection.Send({"action":"message","message":message})

    def Network_disconnected(self, data):
        print 'Server disconnected'
        sys.exit()

    def setMainView(self,mainView):
        self.mainView=mainView
    #Envoie les touches pressees au serveur
    def keys(self,data,map):
        connection.Send({'action':'keys','keystrokes':data,map})

    def Network_move(self, data):
        print 'Mouvement'
        self.jeu.move(data['message']['Joueur'],data['message']['Direction'])

    def Network_rotate(self,data):
        self.jeu.rotate(data['message']['Joueur'])
        
    def getJeu(self):
        return self.jeu
        
