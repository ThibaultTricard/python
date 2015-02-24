import sys
import time
from Client import Client

if len(sys.argv) != 3:
    print "Usage:", sys.argv[0], "host port"
else:
    c = Client(sys.argv[1], int(sys.argv[2]))
    while True:
        c.Loop()
        time.sleep(0.001)
