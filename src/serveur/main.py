#!/usr/bin/env python
# coding: utf-8

from Serveur import MyServer
import sys
import time
import imp
forme = imp.load_source('Forme', '../classes/forme.py')
joueur = imp.load_source('Joueur', '../classes/joueur.py')
carte = imp.load_source('Carte', '../classes/carte.py')


def main_prog():
    my_server = MyServer(localaddr = (sys.argv[1],int(sys.argv[2])))
    while True:
        my_server.Pump()
        time.sleep(0.01)

if __name__ == '__main__':
    main_prog()
    sys.exit(0)
