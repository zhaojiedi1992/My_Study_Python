#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def now():
    print('2024.01.01')

def log(func):
    def wrapper(*args,**kw):
        func_name = func.__name__
        print(f"call {func_name} start")
        return func(*args,**kw)
    return wrapper

now()

@log
def now2():
    print('2024.01.01')

now2()

def now3():
    print('2024.01.01')
now3= log(now3)

now3()