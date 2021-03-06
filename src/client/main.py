import sys
import time
from Client import Client
sys.path.append('/src/client/views/MainView')
from views.MainView import MainView
from views.Accueil import Accueil

def main_prog():
    if len(sys.argv) != 3:
        print "Usage:", sys.argv[0], "host port"
        sys.exit(0)
    else:
        #Creation du client
        client = Client(sys.argv[1], int(sys.argv[2]))
        #Creation de la fenetre principale
        mainView=MainView()
        #permet au client de pouvoir modifier le contenu de la fenetre principale
        client.setMainView(mainView)
        #on cree la page d'accueil
        pageAccueil=Accueil()
        pageAccueil.getAccueilController().setClient(client)
        mainView.setFenetre(pageAccueil.afficherAccueil())
        #le client reste a l'ecoute
        while True:
            client.Loop()
            time.sleep(0.001)

if __name__ == '__main__':
    main_prog()
    sys.exit(0)
