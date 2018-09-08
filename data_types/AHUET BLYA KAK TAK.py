#!/usr/bin/env python

class Test:
	def __init__(self, data):
		self.data = data
	def __hash__(self):
		return None
	def p(self):
		print(self.data)

i = Test
t = i(10)
t.p()
