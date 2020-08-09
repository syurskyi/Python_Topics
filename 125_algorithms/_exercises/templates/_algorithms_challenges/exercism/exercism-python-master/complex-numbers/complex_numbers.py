______ ma__

class ComplexNumber(object
    ___ __init__(self, real, imaginary
        self.real = real
        self.imaginary = imaginary

    ___ __add__(self, other
        r_ ComplexNumber(
                self.real + other.real,
                self.imaginary + other.imaginary)

    ___ __mul__(self, other
        r_ ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real)

    ___ __sub__(self, other
        r_ ComplexNumber(
                self.real - other.real,
                self.imaginary - other.imaginary)

    ___ __truediv__(self, other
        common = abs(other) ** 2
        real = self.real * other.real + self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real - self.real * other.imaginary
        r_ ComplexNumber(real/common, imaginary/common)

    ___ __abs__(self
        r_ (self.real ** 2 + self.imaginary ** 2) ** 0.5

    ___ conjugate(self
        r_ ComplexNumber(self.real, -self.imaginary)

    ___ exp(self
        r_ ComplexNumber(
                # Round needed for floating point errors
                round(ma__.e ** (self.real) * ma__.cos(self.imaginary), 15),
                round(ma__.sin(self.imaginary), 15))

    ___ __eq__(self, other
        r_ self.real __ other.real and self.imaginary __ other.imaginary

    ___ __repr__(self
        r_ "{} + {}i".format(self.real, self.imaginary)
