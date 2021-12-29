_______ random


___ private_key(p):
    r.. random.randint(2, p-1)


___ public_key(p, g, a):
    r.. pow(g, a, p)


___ secret(p, B, a):
    r.. pow(B, a, p)
