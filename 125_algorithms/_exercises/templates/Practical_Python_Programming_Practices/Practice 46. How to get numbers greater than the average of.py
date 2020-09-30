from random import random

x = 10
y =   # list
avg = 0

___ i __ range(x):
    y.append(random())
    print("%5.2f" % y[i], end='')
    avg += y[i]
print()

average = avg/x

print("The everage of the arrary = %.2f" % average)
___ i __ y:
    if i > average:
        print("%4.2f" % i)