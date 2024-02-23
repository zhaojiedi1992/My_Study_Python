import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)
        
@Profiled
def add(a,b):
    return a+b


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

add(1,2)
add(2,3)
print(add.ncalls)

s = Spam()
s.bar(1)
print(Spam.bar.ncalls)