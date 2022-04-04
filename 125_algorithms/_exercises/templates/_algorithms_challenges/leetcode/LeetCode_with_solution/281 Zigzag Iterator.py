"""
Premium Question
"""
__author__ = 'Daniel'


c_ ZigzagIterator(o..
    ___ - , v1, v2
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        mat = [v1, v2]
        maxa = m..((c, r) ___ r, c __ e.. m..(l.... x: l..(x)-1, mat)))
        i = 0
        j = 0
        _reposition()

    ___ _reposition
        w.... i >_ l..(mat) o. j >_ l..(mat[i]
            __ n.. hasNext
                r..

            ____ i >_ l..(mat
                i = 0
                j += 1

            ____ j >_ l..(mat[i]
                i += 1

    ___ next
        """
        :rtype: int
        """
        __ n.. hasNext
            r.. StopIteration

        ret = mat[i][j]
        i += 1
        _reposition()
        r.. ret

    ___ hasNext
        """
        :rtype: bool
        """
        r.. j <_ maxa[0]


__ _______ __ _______
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    itr = ZigzagIterator(v1, v2)
    w.... itr.hasNext
        print itr.next()