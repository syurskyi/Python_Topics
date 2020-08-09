___ countdown_for(start=10
    ___ i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


___ countdown_recursive(start=10
    __ start > 0:
        print(start)
        countdown_recursive(start-1)
    ____
        print('time is up')
