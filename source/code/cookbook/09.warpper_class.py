class A(object):

    def decorator1(self,func):
        def wrapper(*args,**kw):
            print('decorator1')
            return func(*args,**kw)
        return wrapper
    @classmethod
    def decorator2(cls,func):
        def wrapper(*args,**kw):
            print('decorator2')
            return func(*args,**kw)
        return wrapper
    
a = A()

@a.decorator1
def add(a,b):
    return a+b 

@A.decorator2
def add2(a,b):
    return a+b 


print(add(1,2))
print(add2(2,1))