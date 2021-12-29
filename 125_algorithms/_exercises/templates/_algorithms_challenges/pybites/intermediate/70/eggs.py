from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    ___ __init__(self, max) -> None:
        self.max = max
        self.count = 0

    ___ __iter__(self):
        return self

    ___ __next__(self):
        self.count += 1
        __ self.count <= self.max:
            return f"{choice(COLORS)} egg"
        else:
            raise StopIteration

ec = EggCreator(5)

print(next(ec))