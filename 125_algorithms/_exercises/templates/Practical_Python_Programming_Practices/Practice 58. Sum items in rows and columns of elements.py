from random ______ r_i..

col _ 6
row _ 6
matrix _   # list

sum_col _ [0]*col
sum_row _ [0]*row

___ i __ ra..(row):
    myrow _   # list
    ___ j __ ra..(col):
        myrow.ap..(r_i..(0,3))
    matrix.ap..(myrow)

___ i __ ra..(row):
    ___ j __ ra..(col):
        sum_row[i] +_ matrix[i][j]
        sum_col[j] +_ matrix[i][j]

___ i __ ra..(row):
    print(matrix[i], "|", sum_row[i])

print("_" *col*4)
print(sum_col)