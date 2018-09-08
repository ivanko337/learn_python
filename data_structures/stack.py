#!/usr/bin/env python

class Stack:
	def __init__(self):
		self.elements = []
	def push(self, element):
		self.elements.append(element)
	def remove(self):
		return self.elements.pop()
	def p(self, index):
		print(self.elements[index])
	def len(self):
		return len(self.elements)
