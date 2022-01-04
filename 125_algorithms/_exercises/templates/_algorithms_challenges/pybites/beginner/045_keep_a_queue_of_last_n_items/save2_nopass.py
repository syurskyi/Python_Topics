_______ c..


___ my_queue(n=5):
    to_print    # list
    mq = c...d..(maxlen=n)
    ___ i __ r..(n):
        mq.a..(i)
        to_print.a..((i, l..(mq)))
    r.. to_print

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