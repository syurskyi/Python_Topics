from random import random

matrix =   # list

___ i __ range(6):
    row =   # list
    ___ j __ range(6):
        row.append(int(random()*10))
    matrix.append(row)

___ row __ matrix:
    print(row)

rmaxi = 0
rid = 0
i = 0

___ row __ matrix:
    if sum(row) > rmaxi:
        rmaxi = sum(row)
        rid = i
    i += 1
print(rid, '=', rmaxi)

cmaxi = 0
cid = 0
___ i __ range(6):
    sumcol = 0
    ___ j __ range(6):
        sumcol += matrix[j][i]
    if sumcol > cmaxi:
        cmaxi = sumcol
        cid = i
print(cid, '=', cmaxi)