import math


class ComplexNumber(object):
    ___ __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    ___ add(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r, i)

    ___ mul(self, other):
        r = self.real * other.real
        i = self.imaginary * other.imaginary
        return ComplexNumber(r, i)

    ___ sub(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return ComplexNumber(r, i)

    ___ div(self, other):
        d = other.real * other.real + other.imaginary * other.imaginary
        r = (self.real * other.real + self.imaginary *
             other.imaginary) / float(d)
        i = (self.imaginary * other.real - self.real *
             self.real * other.imaginary) / float(d)
        return ComplexNumber(r, i)

    ___ abs(self):
        square_sum = self.real * self.real + self.imaginary * self.imaginary
        return math.sqrt(square_sum)

    ___ conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    ___ exp(self):
        r = round(math.cos(self.imaginary), 8) * math.exp(self.real)
        i = round(math.sin(self.imaginary), 8) * math.exp(self.real)
        return ComplexNumber(r, i)
