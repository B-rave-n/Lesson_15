import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник дробу не може дорівнювати нулю")
        self.a = int(a)
        self.b = int(b)

    def reduction(self):
        gcd = math.gcd(self.a, self.b)
        new = Fraction(self.a/gcd, self.b/gcd)
        return new
    def __float__(self):
        return self.a/self.b

    def __int__(self):
        return self.a // self.b


    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        new = Fraction(a, b)
        return new


    def __add__(self, other):
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        new = Fraction(a, b)
        return new


    def __sub__(self, other):
        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        new = Fraction(a, b)
        return new

    def __truediv__(self, other):
        a = self.a * other.b
        b = self.b * other.a
        new = Fraction(a, b)
        return new

    def __eq__(self, other):
        return self.a*other.b == other.a*self.b

    def __ne__(self, other):
        return self.a * other.b != other.a * self.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"{self.a}/{self.b}"


# Перевірки:
try:
    frt = Fraction(5, 0)
except ValueError as e:
    print(e)

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == '21/18'
f_d = f_b * f_a
assert str(f_d) == '6/18'
f_e = f_a - f_b
assert str(f_e) == '3/18'
f_f = f_a / f_b
assert (f_c/f_e).__float__() == (f_c/f_e).__int__() == 7
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print("Тести пройдено")
print(f"Дроби: {f_a}; {f_b}\nСума: {f_c.reduction()}\nДобуток:{f_d.reduction()}\
\nРізниця: {f_e.reduction()}\nЧастка: {f_f.reduction()}")