____ c.. _______ d..


___ my_queue(n=5):
    r.. d..(maxlen=n)

 
__ _____ __ _____
    mq = my_queue()
    ___ i __ r..(10):
        mq.a..(i)
        print((i, l..(mq)))

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

