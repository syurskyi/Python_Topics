____ collections _______ deque


___ my_queue(n=5):
    r.. deque(maxlen=n)

 
__ __name__ __ '__main__':
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

