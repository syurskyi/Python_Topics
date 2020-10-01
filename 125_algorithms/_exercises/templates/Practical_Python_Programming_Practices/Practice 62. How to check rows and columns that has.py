____ ra__ ______ ra__

row _ 5
col _ 10
matrix _   # list
___ i __ ra..(row):
    myrow _   # list
    ___ j __ ra..(col):
        myrow.ap..(in.(ra__()*50)+10)
    matrix.ap..(myrow)

___ myrow __ matrix:
    print(myrow)

num _ in.(i..("Range of numbers(10-50): "))

print("Rows: ", end_' ')
___ i __ ra..(row):
    __ num __ matrix[i]:
        print(i,end_' ')
print()

print("Columns: ",end_' ')
___ j __ ra..(col):
    ___ i __ ra..(row):
        __ matrix[i][j] __ num:
            print(j, end_' ')
            b..
print()