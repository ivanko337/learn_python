#!/usr/bin/env python3

import socket
from time import sleep

HOST = 'localhost'
PORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

count = 0

while True:
	count += 1
	if count == 100:
		sock.sendall(bytes('STOP', 'utf-8'))
	sock.sendall(bytes('PING', 'utf-8'))
	data = sock.recv(1024).decode()
	if data == 'PONG':
		print('pong')
