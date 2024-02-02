#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_range(start,end):
    if start >=end:
        raise Exception("start >=end ")
    for i in range(start,end):
        yield i 

print(my_range(1,10))

for i in my_range(1,10):
    print(i)