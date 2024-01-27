#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(int("12345",base=8))

def int8(x):
    return int(x,base=8)

print(int8("12345"))

from  functools import partial
int88 = partial(int,base=8)
print(int88("12345"))
