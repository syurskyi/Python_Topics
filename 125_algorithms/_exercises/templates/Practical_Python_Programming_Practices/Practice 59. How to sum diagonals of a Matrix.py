from random import random
row = 5
matrix =   # list

___ i __ ra..(row):
    myrow =   # list
    ___ j __ ra..(row):
        myrow.append(int(random()*10))
    matrix.append(myrow)

___ myrow __ matrix:
    print(myrow)

sum_diagonal1 = 0
sum_diagonal2 = 0

___ i __ ra..(row):
    sum_diagonal1 += matrix[i][i]
    sum_diagonal2 += matrix[i][row-i-1]

print(sum_diagonal1)
print(sum_diagonal2)