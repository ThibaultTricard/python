#!/usr/bin/env python2
# coding: utf-8

from classes import accueil
from classes import jeu
#Connexion au serveur

PORT = 8888
ADRESSE_SERVEUR = '127.0.0.1'

fenetre = accueil.Accueil(ADRESSE_SERVEUR, PORT)
ADRESSE_SERVEUR = fenetre.ADRESSE
PORT = fenetre.PORT
NOM = fenetre.NOM

monJeu= jeu.Jeu(ADRESSE_SERVEUR, PORT, NOM)
monJeu.lancer()
