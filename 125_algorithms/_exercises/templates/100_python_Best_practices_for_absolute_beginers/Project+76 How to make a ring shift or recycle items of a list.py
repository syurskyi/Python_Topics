___ ring_shift(first,next):
    __ next < 0:
        next  abs(next)
        ___ i __ r..(next):
            first.a..(first.pop(0))
    ____:
        ___ i __ r..(next):
            first.insert(0,first.pop())

values  [9,8,7,6,5,4,3,2,1,0]
print(values)

ring_shift(values,-2)
print(values)

ring_shift(values, 3)
print(values)

ring_shift(values, 5)
print(values)