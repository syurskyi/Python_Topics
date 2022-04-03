_______ m__


c_ ComplexNumber(o..
    ___ - , real, imaginary
        real = real
        imaginary = imaginary

    ___ add  other
        r = real + other.real
        i = imaginary + other.imaginary
        r.. ComplexNumber(r, i)

    ___ mul  other
        r = real * other.real
        i = imaginary * other.imaginary
        r.. ComplexNumber(r, i)

    ___ sub  other
        r = real - other.real
        i = imaginary - other.imaginary
        r.. ComplexNumber(r, i)

    ___ div  other
        d = other.real * other.real + other.imaginary * other.imaginary
        r = (real * other.real + imaginary *
             other.imaginary) / f__(d)
        i = (imaginary * other.real - real *
             real * other.imaginary) / f__(d)
        r.. ComplexNumber(r, i)

    ___ abs
        square_sum = real * real + imaginary * imaginary
        r.. m__.sqrt(square_sum)

    ___ conjugate
        r.. ComplexNumber(real, -1 * imaginary)

    ___ exp
        r = r..(m__.cos(imaginary), 8) * m__.exp(real)
        i = r..(m__.sin(imaginary), 8) * m__.exp(real)
        r.. ComplexNumber(r, i)
