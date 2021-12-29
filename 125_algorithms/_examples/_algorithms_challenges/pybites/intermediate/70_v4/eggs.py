from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    ''' Create randomly colored "eggs" '''
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return f'{choice(COLORS)} egg'
        else:
            raise StopIteration
