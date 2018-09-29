#!/usr/bin/env python3
#coding=utf-8

# returns a turtle of two lines from input file
def readFromFile(path):
	f = open(path)
	lines = f.readlines()
	return (lines[0][0:-1], lines[1][0:-1])

def writeToFile(path, lines):
	f = open(path, 'w')
	for line in lines:
		for l in line:
			f.write(l + ' ')
		f.write('\n')

# returns three lists: in first even numbers, in secont - odd numbers, third - None or list of incorrect dates
def sort(dates):
	even = []
	odd  = []
	incorrect = []
	for date in dates:
		if int(date) >= 1 and int(date) <= 31:
			if int(date) % 2 == 0:
				even.append(date)
			else:
				odd.append(date)
		else:
			incorrect.append(date)
	if len(incorrect) == 0:
		incorrect = None
	return (even, odd, incorrect)

# return list of dates
def parse(dates_str):
	return dates_str.split(' ')

dates = readFromFile('input')[1]
dates = parse(dates)
norm  = sort(dates)

even = norm[0]
odd  = norm[1]
udarnik = False

if len(even) > len(odd):
	udarnik = True

lines = [[x for x in even], [x for x in odd], 'YES' if udarnik else 'NO']

writeToFile('output', lines)
