import logging
from functools import wraps

def logged(level,name=None,message=None):
    def decorate(func):
        logname = name if name is not None else func.__module__
        log = logging.getLogger(logname)
        log_msg = message if message is not None else func.__name__

 
        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,log_msg)
            return func(*args,**kwargs)
        return wrapper
    return decorate


@logged(logging.CRITICAL,'example','Adding two numbers')
def add(a,b):
    return a+b 

@logged(logging.CRITICAL)
def add2(a,b):
    return a+b 
add(1,2)
add2(1,2)
