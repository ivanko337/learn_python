class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setNext(self, next):
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
	def add(self, value):
		temp = Node(value)
		temp.setNext(self.head)
		self.head = temp
	def length(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count
	def search(self, value):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == value:
				found = True
			else:
				current = current.getNext()
		return current
	def remove(self, value):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == value:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
	def p(self):
		current = self.head
		while current != None:
			print(current.data)
			current = current.getNext()
