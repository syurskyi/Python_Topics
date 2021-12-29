from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:


    def __init__(self,limit):
        self.limit = limit
        self.i = 0
    
    

    def __next__(self):

        if self.i== self.limit:
            raise StopIteration
        
        self.i += 1
        return choice(COLORS)

    def __iter__(self):
        return self





