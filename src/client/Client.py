#!/usr/bin/env python
# coding: utf-8

import sys
from PodSixNet.Connection import connection, ConnectionListener
import thread
from views.SaisiePseudo import SaisiePseudo
from views.Attente import Attente

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
    def __init__(self, host, port):
        self.Connect((host, port))
        t=thread.start_new_thread(self.Input_loop,())

    def Loop(self):
        connection.Pump()
        self.Pump()

    def Network(self, data):
        print('message de type %s recu' % data['action'])

    ### Network event/message callbacks ###
    def Network_connected(self, data):
        print('connecte au serveur !')

    def Network_message(self,data):
        print(data['message'])

    def Network_error(self, data):
        print 'error:', data['error'][1]
        connection.Close()

    def Network_deconnexion(self,data):
        print "deconnexion"
        connection.close()
        sys.exit()

    """
    Permet au serveur de demander une nouvelle partie : le serveur doit alors
    vérifier qu'il y'a encore des places disponibles afin de générer ou non
    l'écran de login
    """
    def demanderNouvellePartie(self):
        print "Demande nouvelle partie"
        connection.Send({"action":"demandeConnexion"})

    """
    Le serveur a confirmé qu'il y'avait de la place
    Le client va pouvoir saisir son pseudo
    """

    def AttendrePartie(self, pseudo):
        print "envoi du pseudo : " +pseudo
        connection.Send({"action":"username", "username":pseudo})
        self.attente = Attente()
        self.attente.attenteController.setClient(self)
        self.mainView.desinitFenetre()
        self.mainView.setFenetre(attente.ecranAttente())

    def Network_ready(self,data):
        pass

    def Network_confirmationConnexion(self,data):
        saisiePseudo=SaisiePseudo()
        saisiePseudo.saisiePseudoController.setClient(self)
        self.mainView.desinitFenetre()
        self.mainView.setFenetre(saisiePseudo.afficherSaisiePseudo())

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
