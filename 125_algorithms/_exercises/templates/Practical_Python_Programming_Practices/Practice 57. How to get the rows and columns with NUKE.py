____ random _______ random

matrix  []

___ i __ r..(6):
    row  []
    ___ j __ r..(6):
        row.a..(i..(random()*10))
    matrix.a..(row)

___ row __ matrix:
    print(row)

rmaxi  0
rid  0
i  0

___ row __ matrix:
    __ s..(row) > rmaxi:
        rmaxi  s..(row)
        rid  i
    i + 1
print(rid, '=', rmaxi)

cmaxi  0
cid  0
___ i __ r..(6):
    sumcol  0
    ___ j __ r..(6):
        sumcol + matrix[j][i]
    __ sumcol > cmaxi:
        cmaxi  sumcol
        cid  i
print(cid, '=', cmaxi)