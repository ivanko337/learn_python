#!/usr/bin/env python

from queue import Queue
from stack import Stack
from linked_list import LinkedList

def execute_queue():
	temp = Queue()
	for i in range(10):
		temp.add(i)
		temp.p(i)
	print
	print(temp.remove())
	print
	for i in range(temp.len()):
		temp.p(i)

def execute_stack():
	temp = Stack()
        for i in range(10):
		temp.push(i)
                temp.p(i)
        print
        print(temp.remove())
        print
        for i in range(temp.len()):
                temp.p(i)

def execute_list():
	list = LinkedList()
	for i in range(10):
		list.add(i)
	list.p()
	list.remove(5)
	print
	list.p()

execute_list()
