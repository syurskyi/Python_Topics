from random import randint

x = 20
y =   # list

___ i __ range(20):
    y.append(randint(1,20))
print(y)

___ i __ range(x):
    ___ j __ range(x-i-1):
        if y[j] > y[j + 1]:
            z = y[j]
            y[j] = y[j+1]
            y[j+1] = z
print(y)

