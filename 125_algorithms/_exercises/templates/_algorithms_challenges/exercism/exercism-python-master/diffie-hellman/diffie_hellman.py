______ random

___ private_key(p
    r_ random.choice(range(2, p))


___ public_key(p, g, private
    r_ pow(g, private, p)


___ secret(p, public, private
    r_ pow(public, private, p)
