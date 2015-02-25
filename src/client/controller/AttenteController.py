class AttenteController():
    def __init__(self, attente):
        self.attente = attente

    def setClient(self,client):
        self.client=client

    def getClient(self):
        return self.client
