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
#on crée une forme vide
FORM_VIDE = forme.Forme([0,0],[0,0],{0:{},
             1:{},
             2:{},
             3:{}})

#Héritage de la classe Server
class MyServer(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        #on crée un tableau de client
        self.clients = []
        #on crée un tableau de pseudo
        self.pseudos=[]
        #on crée un tableau de Map
        self.MAPS= {0:copy.deepcopy(map.MAP),1:copy.deepcopy(map.MAP),2:copy.deepcopy(map.MAP),3:copy.deepcopy(map.MAP)}
        #on crée un tableau de form avec des formes vides
        self.forms={0:copy.deepcopy(FORM_VIDE),1:copy.deepcopy(FORM_VIDE),2:copy.deepcopy(FORM_VIDE),3:copy.deepcopy(FORM_VIDE)}
        #on crée un tableau pour savoir les joueurs actifs
        self.joueurActifs= []
        #On crée un tableau pour savoir le score des joueurs
        self.scores=[]
        print('Server launched')

    def Connected(self, channel, addr):
        print('New connection')
        self.joueurActifs.append(1)
        self.scores.append(0)
        self.clients.append(channel)

    def del_client(self,channel):
        print('client deconnecte')
        self.clients.remove(channel)

    def getNbClient(self):
        return len(self.clients)

    def getMapParJoueur(self,joueur):
        return self.MAPS[joueur]

    def ajouterPseudo(self,pseudo):
        self.pseudos.append(pseudo)

        #méthode de lancement du jeu
    def launch_game(self):
        # Init Pygame
        print("game launched")
        #on tire des nombre aléatoire pour la formation des block des joueurs
        nbFormeJ0=random.randint(0,6)
        nbFormeJ1=random.randint(0,6)
        nbFormeJ2=random.randint(0,6)
        nbFormeJ3=random.randint(0,6)
        #on récupère un dictionnaire de formes
        dict=dictForme.DictForme()
        formes=dict.getFormes()
        for client in self.clients:
            for i in range(0,len(self.pseudos)):
                #on envoi les pseudo aux joueurs
                client.Send({"action":"pseudo","joueur":i,"pseudo":self.pseudos[i]})
            #on envoie les différente formes aux joueurs
            client.Send({"action":"former","joueur":0,"forme":formes[nbFormeJ0]})
            client.Send({"action":"former","joueur":1,"forme":formes[nbFormeJ1]})
            client.Send({"action":"former","joueur":2,"forme":formes[nbFormeJ2]})
            client.Send({"action":"former","joueur":3,"forme":formes[nbFormeJ3]})
        #on enregistre les formes des joueurs dans un dictionnaire
        self.forms={0:forme.Forme([0,4],[len(formes[nbFormeJ0][0]),4+len(formes[nbFormeJ0][0][0])],formes[nbFormeJ0])
                    ,1:forme.Forme([0,4],[len(formes[nbFormeJ1][0]),4+len(formes[nbFormeJ1][0][0])],formes[nbFormeJ1])
                    ,2:forme.Forme([0,4],[len(formes[nbFormeJ2][0]),4+len(formes[nbFormeJ2][0][0])],formes[nbFormeJ2])
                    ,3:forme.Forme([0,4],[len(formes[nbFormeJ3][0]),4+len(formes[nbFormeJ3][0][0])],formes[nbFormeJ3])}
        #on lance la boucle d'attente
        while True:
            time.sleep(0.01)
            self.Pump()
