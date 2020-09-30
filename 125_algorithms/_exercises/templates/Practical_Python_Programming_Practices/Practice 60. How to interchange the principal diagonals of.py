from random import randint

row = 5
matrix =   # list

___ i __ range(row):
    myrow =   # list
    ___ j __ range(row):
        myrow.append(randint(1,100))
        print("%4d" % myrow[j], end=' ')
    matrix.append(myrow)
    print()
print()

___ i __ range(row):
    x = matrix[i][i]
    matrix[i][i] = matrix[i][row-1-i]
    matrix[i][row-1-i] = x

___ i __ matrix:
    ___ j __ i:
        print("%4d" % j, end=' ')
    print()

