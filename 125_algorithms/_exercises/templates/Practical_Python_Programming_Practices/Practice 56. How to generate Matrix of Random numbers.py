from random import randint

row = 6
col = 6
x =   # list

___ i __ range(row):
    y =   # list
    ___ j __ range(col):
        y.append(randint(1,100))
    x.append(y)
___ i __ x:
    ___ j __ i:
        print("%3d" % j, end=' ')
    print()
