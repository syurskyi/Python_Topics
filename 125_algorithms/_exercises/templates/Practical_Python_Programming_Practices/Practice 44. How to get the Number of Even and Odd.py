import random

x =   # list
___ i __ range(10):
    x.append(int(random.random()*1000))
print(x)

even = odd =0

___ i __ x:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print("The number of even = ", even)
print("The number of odd = ", odd)