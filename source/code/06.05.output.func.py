#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc_sum(*args):
    s=0
    for i in args:
        s+=i
    return s 

def lazy_sum(*args):
    def calc_sum():
        s=0
        for i in args:
            s+=i
        return s 
    return calc_sum

f = lazy_sum
print(f)
print(f(1,2,4))
print(f(1,2,4)())