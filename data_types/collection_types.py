#!/usr/bin/env python3
#coding=utf-8

class Test:
    def __init__(self, data):
        self.data = data
    def __hash__(self):
        return 10

class Test2:
    def __init__(self, data):
        self.data = data
    def __hash__(self):
        return None

t = Test(10)
t2 = Test2(1)
s = {7, "v", t, t2}