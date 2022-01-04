____ r__ _______ choice

COLORS = 'red blue green yellow brown purple'.s.. 


c_ EggCreator:
    ___ - , max) __ N..
        max = max
        count = 0

    ___ __iter__
        r.. self

    ___ __next__
        count += 1
        __ count <= max:
            r.. f"{choice(COLORS)} egg"
        ____:
            r.. StopIteration

ec = EggCreator(5)

print(next(ec))