___ countdown():
    """Write a generator that counts from 100 to 1"""
    t = 100
    while t > 0:
        yield t
        t -= 1