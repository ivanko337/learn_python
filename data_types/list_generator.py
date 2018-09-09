#!/usr/bin/env python3
#coding=utf-8

# [expression for item in iterable]
# [expression for item in iterable if condition]

leaps = [y for y in range(1900, 1940) if y % 4 == 0]
print(leaps)

codes = [s + z + c for s in "MF" for z in "SMLX" for c in "BGW" 
            if not(s == "F" and z == "X")]
print(codes)