import random


___ private_key(p):
    return random.randint(2, p-1)


___ public_key(p, g, a):
    return pow(g, a, p)


___ secret(p, B, a):
    return pow(B, a, p)
