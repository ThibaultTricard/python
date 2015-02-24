#!/usr/bin/env python
# coding: utf-8

import sys
import time
import os
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
    def __init__(self, host, port):
        self.Connect((host, port))
        username=raw_input("Entrez votre pseudo :")
        connection.Send({"action":"username","username":username})
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

    def Input_loop(self):
        while True:
            message=raw_input(">")
            connection.Send({"action":"message","message":message})
           
    def Network_disconnected(self, data):
        print 'Server disconnected'
        sys.exit()

if len(sys.argv) != 3:
    print "Usage:", sys.argv[0], "host port"
else:
    c = Client(sys.argv[1], int(sys.argv[2]))
    while True:
        c.Loop()
        time.sleep(0.001)
