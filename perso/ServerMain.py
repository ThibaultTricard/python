#!/usr/bin/env python
# coding: utf-8

from Serveur import MyServer
import sys
import time
import imp
from classes import forme
from classes import joueur
from classes import carte
NB_CLIENT_NECESSAIRE=2
def main_prog():
    if len(sys.argv)==3:
        launched = False
        my_server = MyServer(localaddr = (sys.argv[1],int(sys.argv[2])))
        while launched==False:
            #quand tout le monde est là on envoie un message a tout le monde
            if len(my_server.pseudos)==NB_CLIENT_NECESSAIRE and launched==False:
                for client in my_server.clients:
                    client.Send({"action":"ready"})
                launched = True
                my_server.launch_game()
            my_server.Pump()
            time.sleep(0.01)
    else:
        print("Erreur de syntaxe: python ServerMain.py adress port")

if __name__ == '__main__':
    main_prog()
    sys.exit(0)
