from random import randint

row = 5
matrix =   # list

___ i __ ra..(row):
    myrow =   # list
    ___ j __ ra..(row):
        myrow.append(randint(1,100))
        print("%4d" % myrow[j], end=' ')
    matrix.append(myrow)
    print()
print()

___ i __ ra..(row):
    x = matrix[i][i]
    matrix[i][i] = matrix[i][row-1-i]
    matrix[i][row-1-i] = x

___ i __ matrix:
    ___ j __ i:
        print("%4d" % j, end=' ')
    print()

