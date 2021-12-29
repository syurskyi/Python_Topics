____ random _______ random
row  5
matrix  []

___ i __ r..(row):
    myrow  []
    ___ j __ r..(row):
        myrow.a..(i..(random()*10))
    matrix.a..(myrow)

___ myrow __ matrix:
    print(myrow)

sum_diagonal1  0
sum_diagonal2  0

___ i __ r..(row):
    sum_diagonal1 + matrix[i][i]
    sum_diagonal2 + matrix[i][row-i-1]

print(sum_diagonal1)
print(sum_diagonal2)