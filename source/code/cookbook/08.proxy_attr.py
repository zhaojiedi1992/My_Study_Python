class A(object): 
    def spam(self, x):
        pass

    def foo(self):
        pass

class B(object):
    def __init__(self) -> None:
        self.a = A()
    def spam(self, x):
        self.a.spam(x)
    def foo(self):
        self.a.foo()

    def bar(self):
            pass
    
a = A()
b = B()
b.spam(1)
b.foo()
b.bar()


class B2:
    """使用__getattr__的代理，代理方法比较多时候"""

    def __init__(self):
        self.a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """这个方法在访问的attribute不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found"""
        return getattr(self.a, name)
    

a = A()
b2 = B2()
b2.spam(1)
b2.foo()
b2.bar()


class Proxy(object):
    def __init__(self,obj) -> None:
        self.obj = obj 
    def __getattr__(self, name):
        return getattr(self.obj,name)
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name,value)
        else:
            setattr(self.obj,name,value)
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            delattr(self.obj,name)