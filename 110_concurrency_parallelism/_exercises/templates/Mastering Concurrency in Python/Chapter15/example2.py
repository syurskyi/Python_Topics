# ch15/example2.py

______ ti..
______ th..

COUNT _ 50000000

___ countdown(n):
    w__ n > 0:
        n -_ 1

###########################################################################

start _ t__.t__()
countdown(COUNT)

print('Sequential program finished.')
print(f'Took {t__.t__() - start : .2f} seconds.')

###########################################################################

thread1 _ ?.T..(target_countdown, args_(COUNT // 2,))
thread2 _ th...T..(target_countdown, args_(COUNT // 2,))

start _ t__.t__()
thread1.s..
thread2.s..
thread1.j..
thread2.j..

print('Concurrent program finished.')
print(f'Took {t__.t__() - start : .2f} seconds.')
