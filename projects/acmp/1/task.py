#!/usr/bin/env python3
#coding=utf-8

def convertTo2(num):
	return str(bin(num)[2:])

def count(s, c):
	return s.count(c)

print(count(convertTo2(13), '1'))
