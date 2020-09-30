from random import random

row = 5
col = 10
matrix =   # list
___ i __ ra..(row):
    myrow =   # list
    ___ j __ ra..(col):
        myrow.append(int(random()*50)+10)
    matrix.append(myrow)

___ myrow __ matrix:
    print(myrow)

num = int(input("Range of numbers(10-50): "))

print("Rows: ", end=' ')
___ i __ ra..(row):
    if num __ matrix[i]:
        print(i,end=' ')
print()

print("Columns: ",end=' ')
___ j __ ra..(col):
    ___ i __ ra..(row):
        if matrix[i][j] == num:
            print(j, end=' ')
            break
print()