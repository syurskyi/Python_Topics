____ r__ _______ randint

col  6
row  6
matrix  []

sum_col  [0]*col
sum_row  [0]*row

___ i __ r..(row):
    myrow  []
    ___ j __ r..(col):
        myrow.a..(randint(0,3))
    matrix.a..(myrow)

___ i __ r..(row):
    ___ j __ r..(col):
        sum_row[i] + matrix[i][j]
        sum_col[j] + matrix[i][j]

___ i __ r..(row):
    print(matrix[i], "|", sum_row[i])

print("_" *col*4)
print(sum_col)