import sys
import time
from classes import client

class Jeu() :
    def __init__(self, ip, port, pseudo):
        self.ip=ip
        self.port=port
        self.pseudo=pseudo

    def lancer(self):
        monClient = client.Client(self.ip, self.port, self.pseudo)
        while True:
            monClient.Loop()
            time.sleep(0.001)
