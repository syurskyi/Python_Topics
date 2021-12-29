from random import random

row  5
col  10
matrix  []
for i in range(row):
    myrow  []
    for j in range(col):
        myrow.append(i..(random()*50)+10)
    matrix.append(myrow)

for myrow in matrix:
    print(myrow)

num  i..(input("Range of numbers(10-50): "))

print("Rows: ", end' ')
for i in range(row):
    __ num in matrix[i]:
        print(i,end' ')
print()

print("Columns: ",end' ')
for j in range(col):
    for i in range(row):
        __ matrix[i][j] __ num:
            print(j, end' ')
            _____
print()