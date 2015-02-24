import sys
import time
from Client import Client
sys.path.append('/src/client/views/MainView')
from views.MainView import MainView

def main_prog():
    if len(sys.argv) != 3:
        main=MainView()
        main.setBackground("../../image/tetris.jpg")
        main.afficherFenetre()
        print "Usage:", sys.argv[0], "host port"
    else:
        c = Client(sys.argv[1], int(sys.argv[2]))
        while True:
            c.Loop()
            time.sleep(0.001)
            
if __name__ == '__main__':
    main_prog()
    sys.exit(0)
