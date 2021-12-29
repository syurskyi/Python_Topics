from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    ___ __init__(self, limit: int):
        self.limit = limit
        self.current = 1

    ___ __iter__(self):
        return self

    ___ __next__(self):
        __ self.current > self.limit:
            raise StopIteration
        self.current += 1
        return f'{choice(COLORS)} egg'
