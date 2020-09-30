from random import random

x = [int(random()*100)___ i __ range(20)]
print(x)

myset = set(x)

highest = None
frequent = 0

___ item __ myset:
    freq = x.count(item)

    if freq > frequent:
        frequent = freq
        highest = item
print(highest)