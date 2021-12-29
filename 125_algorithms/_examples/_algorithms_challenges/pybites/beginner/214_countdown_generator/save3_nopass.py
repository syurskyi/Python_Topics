def countdown():
    """Write a generator that counts from 100 to 1"""
    t = 100
    while True:
        try:
            yield t
            t -= 1
        except StopIteration:
            break