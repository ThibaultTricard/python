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
        c = Client(sys.argv[1], int(sys.argv[2]))
        mainView=MainView()
        mainView.setFenetre(Accueil().getSurface())
        while True:
            c.Loop()
            time.sleep(0.001)
            
if __name__ == '__main__':
    main_prog()
    sys.exit(0)
