#!/usr/bin/env python3
#coding=utf-8

import pickle

#colors = { 'lion':'yellow', 'kity':'red' }

#pickle.dump(colors, open('test', 'wb'))

t = pickle.load(open('test', 'rb'))

print(t)
