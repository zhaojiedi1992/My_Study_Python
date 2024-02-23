class Typed(object):
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value
    def __delete__(self, instance): 
        del instance.__dict__[self.name]
    
def typeassert(**kw):
    def decorate(cls):
        for name, expected_type in kw.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate



@typeassert(name=str,shares=int,price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('a',1,1.0)
s = Stock(1,1,1.0)