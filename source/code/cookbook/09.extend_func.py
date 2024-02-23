import time
from functools import wraps
 
def addtime(func):
    @wraps(func)
    def wrapper(*args,**kw):
        start =time.time()
        result = func(*args,**kw)
        end = time.time()
        print(f'{func.__name__} run time: {end-start}')
        return result
    return wrapper

def addtimev2(func):
    def wrapper(*args,**kw):
        start =time.time()
        result = func(*args,**kw)
        end = time.time()
        print(f'{func.__name__} run time: {end-start}')
        return result
    return wrapper

@addtime
def add(a,b):
    return a+b 
print(add(1,2))

@addtimev2
def add2(a,b):
    return a+b 
print(add2(1,2))

print


