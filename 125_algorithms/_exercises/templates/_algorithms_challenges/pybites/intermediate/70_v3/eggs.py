from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:


    ___ __init__(self,limit):
        self.limit = limit
        self.i = 0
    
    

    ___ __next__(self):

        __ self.i== self.limit:
            raise StopIteration
        
        self.i += 1
        return choice(COLORS)

    ___ __iter__(self):
        return self





