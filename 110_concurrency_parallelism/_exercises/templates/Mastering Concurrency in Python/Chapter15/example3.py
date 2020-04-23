# ch15/example3.py

______ ti..
______ th..
____ m.. ______ Pool

COUNT _ 50000000

___ countdown(n):
    w__ n > 0:
        n -_ 1

__ _______ __ _______

    #######################################################################
    # Sequential

    start _ t__.t__()
    countdown(COUNT)

    print('Sequential program finished.')
    print(f'Took {t__.t__() - start : .2f} seconds.')
    print()

    #######################################################################
    # Multithreading

    thread1 _ ?.T..(target_countdown, args_(COUNT // 2,))
    thread2 _ ?.T..(target_countdown, args_(COUNT // 2,))

    start _ t__.t__()
    thread1.s..
    thread2.s..
    thread1.j..
    thread2.j..

    print('Multithreading program finished.')
    print(f'Took {t__.t__() - start : .2f} seconds.')
    print()

    #######################################################################
    # Multiprocessing

    pool _ Pool(processes_2)
    start _ t__.t__()
    pool.apply_async(countdown, args_(COUNT//2,))
    pool.apply_async(countdown, args_(COUNT//2,))
    pool.c..
    pool.j..

    print('Multiprocessing program finished.')
    print(f'Took {t__.t__() - start : .2f} seconds.')
