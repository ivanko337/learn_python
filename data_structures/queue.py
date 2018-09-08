#!/usr/bin/env python

class Queue:
	def __init__(self):
		self.people = []
	def add(self, person):
		self.people.insert(len(self.people), person)
	def remove(self):
		return self.people.pop(0)
	def p(self, index):
		print(self.people[index])
	def len(self):
		return len(self.people)
