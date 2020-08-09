______ ma__


class ComplexNumber(object
    ___ __init__(self, real, imaginary
        self.real = real
        self.imaginary = imaginary

    ___ add(self, other
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        r_ ComplexNumber(r, i)

    ___ mul(self, other
        r = self.real * other.real
        i = self.imaginary * other.imaginary
        r_ ComplexNumber(r, i)

    ___ sub(self, other
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        r_ ComplexNumber(r, i)

    ___ div(self, other
        d = other.real * other.real + other.imaginary * other.imaginary
        r = (self.real * other.real + self.imaginary *
             other.imaginary) / float(d)
        i = (self.imaginary * other.real - self.real *
             self.real * other.imaginary) / float(d)
        r_ ComplexNumber(r, i)

    ___ abs(self
        square_sum = self.real * self.real + self.imaginary * self.imaginary
        r_ ma__.sqrt(square_sum)

    ___ conjugate(self
        r_ ComplexNumber(self.real, -1 * self.imaginary)

    ___ exp(self
        r = round(ma__.cos(self.imaginary), 8) * ma__.exp(self.real)
        i = round(ma__.sin(self.imaginary), 8) * ma__.exp(self.real)
        r_ ComplexNumber(r, i)
