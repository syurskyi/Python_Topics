from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    ''' Create randomly colored "eggs" '''
    ___ __init__(self, limit):
        self.limit = limit
        self.count = 0

    ___ __iter__(self):
        return self

    ___ __next__(self):
        __ self.count < self.limit:
            self.count += 1
            return f'{choice(COLORS)} egg'
        else:
            raise StopIteration
