___ ring_shift(first,next):
    if next < 0:
        next = abs(next)
        ___ i __ ra..(next):
            first.append(first.pop(0))
    else:
        ___ i __ ra..(next):
            first.insert(0,first.pop())

values = [9,8,7,6,5,4,3,2,1,0]
print(values)

ring_shift(values,-2)
print(values)

ring_shift(values, 3)
print(values)

ring_shift(values, 5)
print(values)