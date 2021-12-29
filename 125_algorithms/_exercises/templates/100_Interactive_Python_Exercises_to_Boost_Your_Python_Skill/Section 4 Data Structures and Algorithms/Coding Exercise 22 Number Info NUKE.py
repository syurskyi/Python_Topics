def foo(number):
    return dict(sign  "positive" __ number > 0 else
        ("negative" __ number < 0 else "zero"),
        parity  "odd" __ number % 2 __ 1 else
        ("even" __ number % 2 __ 0 else "non integer"))