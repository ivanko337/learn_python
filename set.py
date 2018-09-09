#!/usr/bin/env python3
#coding=utf-8

x = set("pecan") | set("pie")
print(x)
x = set("pecan") & set("pie")
print(x)
x = set("pecan") - set("pie")
print(x)
x = set("pecan") ^ set("pie")
print(x)