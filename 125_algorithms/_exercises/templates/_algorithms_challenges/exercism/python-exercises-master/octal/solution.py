___ parse_octal(digits
    digits = _validate_octal(digits)
    r_ sum(int(digit) * 8 ** i
               for (i, digit) in enumerate(reversed(digits)))


___ _validate_octal(digits
    for d in digits:
        __ not '0' <= d < '8':
            raise ValueError("Invalid octal digit: " + d)
    r_ digits
