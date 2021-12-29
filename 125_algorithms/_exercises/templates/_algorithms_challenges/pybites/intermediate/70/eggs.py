____ random _______ choice

COLORS = 'red blue green yellow brown purple'.s.. 


class EggCreator:
    ___ __init__(self, max) -> N..
        self.max = max
        self.count = 0

    ___ __iter__(self):
        r.. self

    ___ __next__(self):
        self.count += 1
        __ self.count <= self.max:
            r.. f"{choice(COLORS)} egg"
        ____:
            raise StopIteration

ec = EggCreator(5)

print(next(ec))