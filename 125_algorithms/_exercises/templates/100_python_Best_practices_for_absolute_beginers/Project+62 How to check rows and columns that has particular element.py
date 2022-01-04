____ r__ _______ r__

row  5
col  10
matrix  []
___ i __ r..(row):
    myrow  []
    ___ j __ r..(col):
        myrow.a..(i..(r__()*50)+10)
    matrix.a..(myrow)

___ myrow __ matrix:
    print(myrow)

num  i..(input("Range of numbers(10-50): "))

print("Rows: ", end' ')
___ i __ r..(row):
    __ num __ matrix[i]:
        print(i,end' ')
print()

print("Columns: ",end' ')
___ j __ r..(col):
    ___ i __ r..(row):
        __ matrix[i][j] __ num:
            print(j, end' ')
            _____
print()