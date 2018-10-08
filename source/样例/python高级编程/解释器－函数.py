from functools import wraps
def my_decorator(function):
    @wraps(function)
    def wrapped(*args,**kwargs):
        """   this is test wrapped """
        print( "start")
        result=function(*args,**kwargs)
        print( "end")
        return result
    return wrapped

@my_decorator
def foo():
    """
    this is test foo
    :return:
    """
    print("abc")


foo()
print(foo.__name__)
print(foo.__doc__)