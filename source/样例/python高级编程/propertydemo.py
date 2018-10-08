class Rectangle():
    def __init__(self,x1,x2,y1,y2):
        self.x1, self.x2 = x1, x2
        self.y1, self.y2 = y1, y2

    @property
    def width(self):
        return self.x2 - self.x1
    @width.setter
    def width(self,value):
        self.x2 = self.x1 + value
    @property
    def height(self):
        return self.y2 - self.y1


rec = Rectangle(1,2,3,5)

print(rec.width)
rec.width=10
print(rec.width)