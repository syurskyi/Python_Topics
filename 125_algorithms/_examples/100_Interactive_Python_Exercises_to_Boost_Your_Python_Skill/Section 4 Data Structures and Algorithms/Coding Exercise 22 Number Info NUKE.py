def foo(number):
    return dict(sign = "positive" if number > 0 else
        ("negative" if number < 0 else "zero"),
        parity = "odd" if number % 2 == 1 else
        ("even" if number % 2 == 0 else "non integer"))