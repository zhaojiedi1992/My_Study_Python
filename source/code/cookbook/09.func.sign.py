from inspect import Signature, Parameter

# Make a signature for a func(x, y=42, *, z=None)
sig = Signature(
    [
        Parameter('x',Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('y',Parameter.POSITIONAL_OR_KEYWORD,default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None) 

    ]
)


print(sig)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name,value)

func(1,2,z=3)


def make_sig(*names):
    return Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names])

class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields',[]))
        return super().__new__(cls, clsname, bases, clsdict)
    
class Structure(metaclass=StructureMeta):
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

class Point(Structure):
   _fields = ['x','y']


p = Point(1,2)
print(p.x,p.y)

