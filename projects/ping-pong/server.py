#!/usr/bin/env python3
#coding=utf-8

import socketserver
from time import sleep

HOST = 'localhost'
PORT = 4444

class Handler(socketserver.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024).decode()

		while True:
			if self.data == 'PING':
				print('ping')
				self.request.sendall(bytes('PONG', 'utf-8'))
			if self.data == 'STOP':
				print('stop')
				break
			sleep(5)

server = socketserver.TCPServer((HOST, PORT), Handler)
print('Server running')

server.serve_forever()
