from functools import wraps,partial
import logging

def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name is not None else func.__module__
        log = logging.getLogger(logname)
        log_msg = message if message is not None else func.__name__

 
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func
        
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel
        # wrapper.set_level = set_level
        
        @attach_wrapper(wrapper)
        def set_name(newname):
            nonlocal logname
            logname = newname
        # wrapper.set_name = set_name
        
        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal log_msg
            log_msg = newmsg
        # wrapper.set_message = set_message

        return wrapper
    return decorate 


@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


import logging
logging.basicConfig(level=logging.DEBUG)
add(2, 3)
add.set_message('Add called')
add(2,3)


# add_3 = logged(level,name,message)(add)()
