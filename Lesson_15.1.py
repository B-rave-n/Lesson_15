class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __add__(self, other):
        # a = self.width
        # b = other.get_area()/self.width+self.height
        area = other.get_area() + self.get_area()
        a = self.width
        b = area/a
        new = Rectangle(a, b)
        return new

    def __mul__(self, n):
        a = self.width * n
        b = self.height
        new = Rectangle(a, b)
        return new

    def __str__(self):
        return f"Довжина: {self.width}. Ширина: {self.height}. Площа: {self.get_area()}."

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_area() == 8, 'Test1'
assert r2.get_area() == 18, 'Test2'

r3 = r1 + r2
# print(r3)
assert r3.get_area() == 26, 'Test3'

r4 = r1 * 4
# print(r4)
assert r4.get_area() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'