____ ra__ ______ r_i..

row _ 5
matrix _   # list

___ i __ ra..(row):
    myrow _   # list
    ___ j __ ra..(row):
        myrow.ap..(r_i..(1,100))
        print("%4d" % myrow[j], end_' ')
    matrix.ap..(myrow)
    print()
print()

___ i __ ra..(row):
    x _ matrix[i][i]
    matrix[i][i] _ matrix[i][row-1-i]
    matrix[i][row-1-i] _ x

___ i __ matrix:
    ___ j __ i:
        print("%4d" % j, end_' ')
    print()

