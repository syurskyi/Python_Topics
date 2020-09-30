___ rebase(input_base, digits, output_base
    r_ to_base(from_base(digits, input_base), output_base)

___ from_base(digits, base
    result = 0
    __ base < 2:
        raise ValueError("Not a valid base: {}".format(base))
    ___ digit __ digits:
        __ not (0 <= digit < base
            raise ValueError("Not a valid digit in base {}: {}".format(base, digit))
        result = result * base + digit
    r_ result

___ to_base(number, base
    digits =   # list
    __ base < 2:
        raise ValueError("Not a valid base: {}".format(base))
    w___ number > 0:
        digits.insert(0, number % base)
        number //= base
    r_ digits
