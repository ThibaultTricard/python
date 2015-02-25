#!/usr/bin/env python
# coding: utf-8
class SaisiePseudoController:
    def __init__(self,saisiePseudo):
        self.saisiePseudo=saisiePseudo

    def setClient(self,client):
        self.client=client

    def getClient(self):
        return self.client

    def envoyerPseudo(self, pseudo):
        self.client.AttendrePartie(pseudo)
