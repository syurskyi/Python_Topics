from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    
    def __init__(self, limit):
        self._limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self._limit > 0:
            self._limit -= 1
            return choice(COLORS)
        else:
            raise StopIteration


#if __name__ == "__main__":
    #egg = EggCreator(4)
    #print(len(egg))
    #print(list(egg))
    #print(len(list(egg)))