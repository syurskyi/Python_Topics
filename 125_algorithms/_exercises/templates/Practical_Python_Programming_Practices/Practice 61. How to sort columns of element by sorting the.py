____ ra__ ______ r_i..
col _ 6
row _ 3
matrix _   # list
___ i __ ra..(row):
    myrow _   # list
    ___ j __ ra..(col):
        myrow.ap..(r_i..(10,100))
    matrix.ap..(myrow)
___ i __ matrix:
    print(i)
print()
k _ col-1
w___ k !_ 0:
    z _ 0
    ___ j __ ra..(1, k+1):
        __ matrix[0][j] > matrix[0][z]:
            z _ j
    ___ i __ ra..(row):
        y _ matrix[i][z]
        matrix[i][z] _ matrix[i][k]
        matrix[i][k] _ y
    k -_ 1
___ i __ matrix:
    print(i)