____ random _______ choice

COLORS = 'red blue green yellow brown purple'.s.. 


class EggCreator:
    ___ __init__(self, limit: int):
        self.limit = limit
        self.current = 1

    ___ __iter__(self):
        r.. self

    ___ __next__(self):
        __ self.current > self.limit:
            raise StopIteration
        self.current += 1
        r.. f'{choice(COLORS)} egg'
