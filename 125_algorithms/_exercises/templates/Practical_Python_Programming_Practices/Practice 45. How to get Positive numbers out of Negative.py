import random

x =   # list
___ i __ ra..(20):
    x.append(int(random.random()*20)-10)
print(x)

pos =   # list
neg =   # list

___ i __ x:
    if i<0:
        neg.append(i)
    elif i>0:
        pos.append(i)
print("Negative numbers = ",neg)
print("Positive numbers = ",pos)