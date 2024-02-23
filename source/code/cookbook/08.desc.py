class Interger(object):
    def __init__(self,name):
        self.name =name 
    def __get__(self,instance,cls):
        if instance is None:
            return self 
        return instance.__dict__[self.name]
    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self,instance):
        del instance.__dict__[self.name]

class Point(object):
    x = Interger('x')
    y = Interger('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
p.x =5 
print(p.x)

p2= Point(4,5)
print(p2.x)
print(p.x)
    