____ random _______ choice

COLORS = 'red blue green yellow brown purple'.s..


class EggCreator:
    ''' Create randomly colored "eggs" '''
    ___ __init__(self, limit):
        self.limit = limit
        self.count = 0

    ___ __iter__(self):
        r.. self

    ___ __next__(self):
        __ self.count < self.limit:
            self.count += 1
            r.. f'{choice(COLORS)} egg'
        ____:
            raise StopIteration
