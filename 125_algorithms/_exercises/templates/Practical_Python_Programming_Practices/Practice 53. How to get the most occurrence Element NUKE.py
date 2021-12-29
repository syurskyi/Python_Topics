from random import random

x  [i..(random()*100)for i in range(20)]
print(x)

myset  set(x)

highest  N..
frequent  0

for item in myset:
    freq  x.count(item)

    __ freq > frequent:
        frequent  freq
        highest  item
print(highest)