____ r__ _______ randint

x  20
y  []

___ i __ r..(20):
    y.a..(randint(1,20))
print(y)

___ i __ r..(x):
    ___ j __ r..(x-i-1):
        __ y[j] > y[j + 1]:
            z  y[j]
            y[j]  y[j+1]
            y[j+1]  z
print(y)

