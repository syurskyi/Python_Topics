# ch12/example1.py

______ th..
______ ti..

___ thread_a():
    print('Thread A is starting...')

    print('Thread A waiting to acquire lock A.')
    lock_a.a..
    print('Thread A has acquired lock A, performing some calculation...')
    t__.s..(2)

    print('Thread A waiting to acquire lock B.')
    lock_b.a..
    print('Thread A has acquired lock B, performing some calculation...')
    t__.s..(2)

    print('Thread A releasing both locks.')
    lock_a.release()
    lock_b.release()

___ thread_b():
    print('Thread B is starting...')

    print('Thread B waiting to acquire lock B.')
    lock_b.a..
    print('Thread B has acquired lock B, performing some calculation...')
    t__.s..(5)

    print('Thread B waiting to acquire lock A.')
    lock_a.a..
    print('Thread B has acquired lock A, performing some calculation...')
    t__.s..(5)

    print('Thread B releasing both locks.')
    lock_b.release()
    lock_a.release()

lock_a _ ?.Lock()
lock_b _ ?.Lock()

thread1 _ ?.T..(target_thread_a)
thread2 _ ?.T..(target_thread_b)

thread1.s..
thread2.s..

thread1.j..
thread2.j..

print('Finished.')
