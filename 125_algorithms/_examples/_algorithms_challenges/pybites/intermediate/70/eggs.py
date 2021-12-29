from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, max) -> None:
        self.max = max
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.max:
            return f"{choice(COLORS)} egg"
        else:
            raise StopIteration

ec = EggCreator(5)

print(next(ec))