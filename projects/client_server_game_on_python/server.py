#!/usr/bin/env python3
#coding=utf-8

import random
import socketserver

HOST = 'localhost'
PORT = 4444

class GibbetHandler(socketserver.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024).decode()
		print("Client {} send {}".format(self.client_address[0], self.data))

		rand = random.randint(1, 100)

		if self.data == 'START':
			self.request.sendall(bytes('GUESS;1;100', 'utf-8'))
			try_count = 10
			while True:
				self.data = self.request.recv(1024).decode()
				data = self.data.split(';')
				if data[0] == 'TRY':
					if int(data[1]) == rand:
						self.request.sendall(bytes('TRUE', 'utf-8'))
						break
					else:
						try_count -= 1
						if try_count == 0:
							self.request.sendall(bytes('FAIL', 'utf-8'))
							break
						else:
							self.request.sendall(bytes('FALSE', 'utf-8'))
				elif data[0] == 'GOODBYE':
					print('Client disconnected')
					break

server = socketserver.TCPServer((HOST, PORT), GibbetHandler)
print('Server running')

server.serve_forever()
