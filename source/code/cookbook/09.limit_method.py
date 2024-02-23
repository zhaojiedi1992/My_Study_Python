class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if  name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)

class NoMixedCase(metaclass=NoMixedCaseMeta):
     
     def a(self):
          pass
     def AbcD(self):
          pass
     
c = NoMixedCase()
c.AbcD()