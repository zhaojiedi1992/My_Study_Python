#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_odd(a):
    if a%2==0:
        return True
    return False 

list(filter(is_odd,range(1,10)))