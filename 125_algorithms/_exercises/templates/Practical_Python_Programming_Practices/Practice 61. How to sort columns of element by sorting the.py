from random import randint
col = 6
row = 3
matrix =   # list
___ i __ range(row):
    myrow =   # list
    ___ j __ range(col):
        myrow.append(randint(10,100))
    matrix.append(myrow)
___ i __ matrix:
    print(i)
print()
k = col-1
while k != 0:
    z = 0
    ___ j __ range(1, k+1):
        if matrix[0][j] > matrix[0][z]:
            z = j
    ___ i __ range(row):
        y = matrix[i][z]
        matrix[i][z] = matrix[i][k]
        matrix[i][k] = y
    k -= 1
___ i __ matrix:
    print(i)