from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Debug Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper

@optional_debug
def add(a,b):
    return a+b 



add(1,2,debug=True)