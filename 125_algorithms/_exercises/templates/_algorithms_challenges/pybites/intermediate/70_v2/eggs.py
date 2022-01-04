____ random _______ choice

COLORS = 'red blue green yellow brown purple'.s.. 


c_ EggCreator:
    
    ___ - , limit):
        _limit = limit

    ___ __iter__
        r.. self

    ___ __next__
        __ _limit > 0:
            _limit -= 1
            r.. choice(COLORS)
        ____:
            r.. StopIteration


#if __name__ == "__main__":
    #egg = EggCreator(4)
    #print(len(egg))
    #print(list(egg))
    #print(len(list(egg)))