____ random _______ randint
col  6
row  3
matrix  []
___ i __ r..(row):
    myrow  []
    ___ j __ r..(col):
        myrow.a..(randint(10,100))
    matrix.a..(myrow)
___ i __ matrix:
    print(i)
print()
k  col-1
w___ k ! 0:
    z  0
    ___ j __ r..(1, k+1):
        __ matrix[0][j] > matrix[0][z]:
            z  j
    ___ i __ r..(row):
        y  matrix[i][z]
        matrix[i][z]  matrix[i][k]
        matrix[i][k]  y
    k - 1
___ i __ matrix:
    print(i)