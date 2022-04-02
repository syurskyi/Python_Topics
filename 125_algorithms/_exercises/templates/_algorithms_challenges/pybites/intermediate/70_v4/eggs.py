____ r__ _______ choice

COLORS = 'red blue green yellow brown purple'.s..


c_ EggCreator:
    ''' Create randomly colored "eggs" '''
    ___ - , limit
        limit = limit
        count = 0

    ___ __iter__
        r.. self

    ___ __next__
        __ count < limit:
            count += 1
            r.. f'{choice(COLORS)} egg'
        ____:
            r.. StopIteration
