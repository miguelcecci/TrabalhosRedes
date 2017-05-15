#!/usr/bin/env python

# client.py
import socket
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = '127.0.1.1'
port = raw_input("Digite a porta:")

# connection to hostname on the port.
s.connect((host, int(port)))

def recvall(sock):
	BUFF_SIZE = 1024 # 4 KiB
	data = ""
	while True:
		part = sock.recv(BUFF_SIZE)
		data += part
		if '---' in part:
			break
	return data

while 1:
	print('Digite:')
	print("> 0 - listar as timezones disponiveis")
	print("> 'Nome da timezone' - consultar uma timezone")
	opc = raw_input(">")
	s.send(opc)
	if opc == "CLOSE":
		break
	print(recvall(s))

	# chunk = s.recv(1024)
	# chunk = chunk
	# print chunk

s.close()


#fontes
# http://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
