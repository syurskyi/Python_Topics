from random import randint

col = 6
row = 6
matrix =   # list

sum_col = [0]*col
sum_row = [0]*row

___ i __ ra..(row):
    myrow =   # list
    ___ j __ ra..(col):
        myrow.append(randint(0,3))
    matrix.append(myrow)

___ i __ ra..(row):
    ___ j __ ra..(col):
        sum_row[i] += matrix[i][j]
        sum_col[j] += matrix[i][j]

___ i __ ra..(row):
    print(matrix[i], "|", sum_row[i])

print("_" *col*4)
print(sum_col)