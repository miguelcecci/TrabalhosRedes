#!/usr/bin/env python

# server.py
import socket
from pytz import timezone, all_timezones
from datetime import *

port = raw_input("Digite a porta:")
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
# bind to the port
serversocket.bind((host, int(port)))
# queue up to 5 requests
serversocket.listen(5)
print('Servidor rodando...')
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    value = clientsocket.recv(1024)
    if value == "0":
        for i in range(0, 501):
            clientsocket.send(all_timezones[i]+'\n')
        clientsocket.send("---")
    else:
        if value in all_timezones:
            aux = str('Horario de '+str(value)+' - '+str(datetime.now(timezone(value))))
            clientsocket.send(aux)
            clientsocket.send("---")
            print(aux)
        else:
            clientsocket.send("O valor digitado nao consta na lista de timezones")
            clientsocket.send("---")
    clientsocket.close()
