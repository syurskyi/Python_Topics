from string import ascii_uppercase


___ sequence_generator():
    while True:
        for a in enumerate(ascii_uppercase, start=1):
            yield a[0]
            yield a[1]
