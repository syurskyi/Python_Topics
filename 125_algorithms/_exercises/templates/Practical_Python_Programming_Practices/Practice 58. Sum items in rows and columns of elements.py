from random import randint

col = 6
row = 6
matrix =   # list

sum_col = [0]*col
sum_row = [0]*row

___ i __ range(row):
    myrow =   # list
    ___ j __ range(col):
        myrow.append(randint(0,3))
    matrix.append(myrow)

___ i __ range(row):
    ___ j __ range(col):
        sum_row[i] += matrix[i][j]
        sum_col[j] += matrix[i][j]

___ i __ range(row):
    print(matrix[i], "|", sum_row[i])

print("_" *col*4)
print(sum_col)