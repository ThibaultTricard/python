#!/usr/bin/env python
# coding: utf-8

import sys
from PodSixNet.Connection import connection, ConnectionListener
import thread

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

    def Loop(self):
        connection.Pump()
        self.Pump()

    def Network(self, data):
        print('message de type %s recu' % data['action'])

    ### Network event/message callbacks ###
    def Network_connected(self, data):
        print('connecte au serveur !')
        connection.Send({"action":"username","username":self.pseudo})

    #Recupere le pseudo du joueur au serveur
    def Network_pseudo(self,data):
        self.jeu.setPseudoJoueur(data["joueur"],data["pseudo"])

    #Confirme de connexion au serveur
    def Network_confirmationConnexion(self,data):
        print "Confirmation connexion"

    def Network_message(self,data):
        print(data['message'])

    def Network_error(self, data):
        print 'error:', data['error'][1]
        connection.Close()

    #Gere si le serveur est complet
    def Network_connexionRefusee(self,data):
        print "Desole plus de place !"
        sys.exit()

    #Gere la fin du jeu
    def Network_fin(self,data) :
        self.jeu.gagnant=data['gagnant']
        self.jeu.end = True

    #A la demande du serveur creer une forme pour un joueur
    def Network_former(self,data):
        print "former"
        print str(data)
        connection.Send({"action":"former","forme":data["forme"]})
        self.jeu.create(data["joueur"],data["forme"])

    #A la demande du serveur pose la forme active
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

    #A la demande du serveur commence la partie
    def Network_ready(self,data):
        self.jeu.commencer()

    #Gere la deconnection du serveur
    def Network_disconnected(self, data):
        print 'Server disconnected'
        sys.exit()

    def setMainView(self,mainView):
        self.mainView=mainView

    #Envoie les touches pressees au serveur
    def keys(self,data):
        connection.Send({'action':'keys','keystrokes':data})

    #Envoie au serveur une demande de descente automatique
    def down(self):
        connection.Send({'action':'down'})

    #A la demande du serveur augmente le score d'un joueur
    def Network_augmenterScore(self,data):
        self.jeu.augmenterScore(data["Joueur"],data["score"])

    #A la demande du serveur redessiner la map
    def Network_refreshMap(self,data):
        self.jeu.refresh(data['message']['Joueur'],data['message']['MAP'])

    #A la demande du serveur gere les mouvements de la forme active
    def Network_move(self, data):
        print 'Mouvement'
        self.jeu.move(data['message']['Joueur'],data['message']['Direction'])

    #A la demande du serveur gere les rotations de la forme active
    def Network_rotate(self,data):
        self.jeu.rotate(data['message']['Joueur'])

    def demanderMap(self):
        connection.Send({"action":"rafraichir"})

    def miseAJourMap(self):
        connection.Send({"action":"miseAJourMap","map":self.MAP})

    def getJeu(self):
        return self.jeu
