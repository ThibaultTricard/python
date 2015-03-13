#!/usr/bin/env python2
# coding: utf-8

from classes import accueil
from classes import jeu
#Connexion au serveur

PORT = 8888
ADRESSE_SERVEUR = '127.0.0.1'
#on créer une fenètre d'acceuil
fenetre = accueil.Accueil(ADRESSE_SERVEUR, PORT)
#on récupère les valeurs entrées dans la fenètre d'acceuil
ADRESSE_SERVEUR = fenetre.ADRESSE
PORT = fenetre.PORT
NOM = fenetre.NOM
#on crée le jeu
monJeu= jeu.Jeu(ADRESSE_SERVEUR, PORT, NOM)
#on lance le jeu
monJeu.lancer()
