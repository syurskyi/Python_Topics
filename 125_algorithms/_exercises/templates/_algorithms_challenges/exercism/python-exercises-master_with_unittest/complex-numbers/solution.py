_______ math


c_ ComplexNumber(object):
    ___ - , real, imaginary):
        real = real
        imaginary = imaginary

    ___ add(self, other):
        r = real + other.real
        i = imaginary + other.imaginary
        r.. ComplexNumber(r, i)

    ___ mul(self, other):
        r = real * other.real
        i = imaginary * other.imaginary
        r.. ComplexNumber(r, i)

    ___ sub(self, other):
        r = real - other.real
        i = imaginary - other.imaginary
        r.. ComplexNumber(r, i)

    ___ div(self, other):
        d = other.real * other.real + other.imaginary * other.imaginary
        r = (real * other.real + imaginary *
             other.imaginary) / float(d)
        i = (imaginary * other.real - real *
             real * other.imaginary) / float(d)
        r.. ComplexNumber(r, i)

    ___ abs
        square_sum = real * real + imaginary * imaginary
        r.. math.sqrt(square_sum)

    ___ conjugate
        r.. ComplexNumber(real, -1 * imaginary)

    ___ exp
        r = round(math.cos(imaginary), 8) * math.exp(real)
        i = round(math.sin(imaginary), 8) * math.exp(real)
        r.. ComplexNumber(r, i)
