from random import randint

x = 20
y =   # list

___ i __ ra..(20):
    y.append(randint(1,20))
print(y)

j = x-1
while j != 0:
    k = 0
    ___ i __ ra..(1, j+1):
        if y[i] > y[k]:
            k = i
    z = y[k]
    y[k] = y[j]
    y[j] = z
    j -= 1
print(y)