____ random _______ randint

row  5
matrix  []

___ i __ r..(row):
    myrow  []
    ___ j __ r..(row):
        myrow.a..(randint(1,100))
        print("%4d" % myrow[j], end' ')
    matrix.a..(myrow)
    print()
print()

___ i __ r..(row):
    x  matrix[i][i]
    matrix[i][i]  matrix[i][row-1-i]
    matrix[i][row-1-i]  x

___ i __ matrix:
    ___ j __ i:
        print("%4d" % j, end' ')
    print()

