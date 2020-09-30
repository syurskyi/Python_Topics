from random ______ random
row _ 5
matrix _   # list

___ i __ ra..(row):
    myrow _   # list
    ___ j __ ra..(row):
        myrow.ap..(in.(random()*10))
    matrix.ap..(myrow)

___ myrow __ matrix:
    print(myrow)

sum_diagonal1 _ 0
sum_diagonal2 _ 0

___ i __ ra..(row):
    sum_diagonal1 +_ matrix[i][i]
    sum_diagonal2 +_ matrix[i][row-i-1]

print(sum_diagonal1)
print(sum_diagonal2)