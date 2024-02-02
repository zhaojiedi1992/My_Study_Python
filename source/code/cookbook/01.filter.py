#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = [1, 4, -5, 10, -7, 2, 3, -1]
print([x for x in a if x>0])

b = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(s): 
    try : 
        _= int(s)
    except: 
        return False
    return True

c = list(filter(is_int, b))
print(c)


import itertools

Codes =['C', 'C++', 'Java', 'Python'] 
selectors = [False, False, False, True] 
  
Best_Programming = itertools.compress(Codes, selectors) 
  
for each in Best_Programming: 
    print(each) 
