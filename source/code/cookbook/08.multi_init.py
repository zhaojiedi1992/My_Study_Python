import math

class Structure1:
    fields = []

    def __init__(self, *args):
        if len(args) != len(self.fields):
            raise TypeError('Expected {} arguments'.format(len(self.fields)))
        for name, value in zip(self.fields, args):
            setattr(self, name, value)
class Point(Structure1):
    fields = ['x', 'y']

class Circle(Structure1):
    fields = ['radius']
    def area(self):
        return math.pi * self.radius ** 2
    

p = Point(1,2)
print(p.x   )
c = Circle(3)
print(c.area())