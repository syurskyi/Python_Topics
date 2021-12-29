def countdown():
    """Write a generator that counts from 100 to 1"""
    t = 100
    while t > 1:
        print(t)
        t -= 1
    return t