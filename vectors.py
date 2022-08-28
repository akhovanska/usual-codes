from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):  # representation as number without 'e' and else
        return 'vector(%r, %r)' % (self.x, self.y)  # % - modulo operator that is left which dividing, r - raw formal
        # for debugging; %r = str.format

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):  # if modul vector = 0, return false
        return bool(abs(self))

    # Vector.__bool__:
    # def __bool__(self):
    # return bool(self.x or self.y)

    def __add__(self, other):  # +
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):  # *
        return Vector(self.x * scalar, self.y * scalar)
