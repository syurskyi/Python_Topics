____ random _______ randint

x  20
y  []

___ i __ r..(20):
    y.a..(randint(1,20))
print(y)

j  x-1
w___ j ! 0:
    k  0
    ___ i __ r..(1, j+1):
        __ y[i] > y[k]:
            k  i
    z  y[k]
    y[k]  y[j]
    y[j]  z
    j - 1
print(y)