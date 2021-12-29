___ countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


___ countdown_recursive(start=10):
    __ start == 0:
        print("time is up")
    else:
        print(start)
        countdown_recursive(start-1)