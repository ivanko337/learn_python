#!/usr/bin/env python3
#coding=utf-8

import socket

HOST = 'localhost'
PORT = 4444

print('Hello!')
print('Connecting to server {}:{}'.format(HOST, PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(bytes('START', 'utf-8'))

data = sock.recv(1024).decode()
data = data.split(';')

if data[0] == 'GUESS':
	print('Guess number bigger then {} and less then {}. You have 10 tries'.format(data[1], data[2]))
	while True:
		num = input('enter your answer ')
		if num == 'q':
			break
		sock.sendall(bytes('TRY;{}'.format(num), 'utf-8'))
		data = sock.recv(1024).decode().split(';')

		if data[0] == 'TRUE':
			print('You are win!')
			break
		elif data[0] == 'FALSE':
			print('You did not guess. You have any times..')
		elif data[0] == 'FAIL':
			print('You are lose')
			break

sock.sendall(bytes('GOODBYE', 'utf-8'))

sock.close()
