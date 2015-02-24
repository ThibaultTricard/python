#!/usr/bin/env python
# coding: utf-8
import sys
from Serveur import MyServer
import time
def main_prog():
    my_server = MyServer(localaddr = (sys.argv[1],int(sys.argv[2])))
    while True:
        my_server.Pump()
        time.sleep(0.01)

if __name__ == '__main__':
    main_prog()
    sys.exit(0)

