import collections


___ my_queue(n=5):
    to_print = []
    mq = collections.deque(maxlen=n)
    for i in range(n):
        mq.append(i)
        to_print.append((i, list(mq)))
    return to_print

    """Queue size does not go beyond n int, this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """