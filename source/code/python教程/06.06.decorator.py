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


# 设计一个计时器装饰圈
import time ,functools

def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start =  time.time()
        res = func(*args,**kw)
        end = time.time()
        print("exec <{}> time: {}".format(func.__name__,end-start))
        return res 
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


fast(1,2)

