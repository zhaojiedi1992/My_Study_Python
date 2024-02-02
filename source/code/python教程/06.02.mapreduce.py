#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x * x 

r = map(f,[1,2,3])
print(list(r))

from functools import reduce

def add (a,b):
    return a+b 

print(reduce(add,range(1,101)))

# str to int 

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x,y):
        return x*10 +y 
    def char2num(ch):
        return DIGITS[ch]
    return reduce(fn,map(char2num,s))