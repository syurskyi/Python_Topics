____ ra__ ______ ra__

matrix _   # list

___ i __ ra..(6):
    row _   # list
    ___ j __ ra..(6):
        row.ap..(in.(ra__()*10))
    matrix.ap..(row)

___ row __ matrix:
    print(row)

rmaxi _ 0
rid _ 0
i _ 0

___ row __ matrix:
    __ su.(row) > rmaxi:
        rmaxi _ su.(row)
        rid _ i
    i +_ 1
print(rid, '=', rmaxi)

cmaxi _ 0
cid _ 0
___ i __ ra..(6):
    sumcol _ 0
    ___ j __ ra..(6):
        sumcol +_ matrix[j][i]
    __ sumcol > cmaxi:
        cmaxi _ sumcol
        cid _ i
print(cid, '=', cmaxi)