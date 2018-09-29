#!/usr/bin/env python3
#coding=utf-8

hair = "black", "brown", "blonde", "red"
print(hair[2])
print(hair[-3:]) # тоже самое что и hair[1:]

# добавление нового элемента в кортеж
hair = hair[:2] + ("gray",) + hair[2:]
print(hair)

