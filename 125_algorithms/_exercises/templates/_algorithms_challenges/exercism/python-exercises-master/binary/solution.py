___ parse_binary(digits
    __ set(digits) - set('01'
        raise ValueError("Invalid binary literal: " + digits)
    r_ sum(int(digit) * 2 ** i
               for (i, digit) in enumerate(reversed(digits)))
