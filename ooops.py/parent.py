class Shape():
    name: str
    def __init__(self, name):
        self.name = name
class Rectangle(Shape):
    l: int
    b: int
    def __init__(self, name, l, b):
        super().__init__(name)
        self.l = l
        self.b = b
    def area(self):
        result = self.l * self.b
        print(result)
class Circle(Shape):
    r:int
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r
    def area(self):
        result = 3.14*self.r**2
        print(result)

r1 = Rectangle("rectangle", 4,3)
r1.area()

c2 = Circle("circle", 4)
c2.area()

