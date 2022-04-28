c_ Solution:
    ___ dominantIndex  A
        """
        :type A: List[int]
        :rtype: int
        """

        _max __max f__ '-inf'
        _max_i -1

        ___ i __ r..(l..(A:
            __ A[i] > _max:
                __max _max
                _max A[i]
                _max_i i
                _____

            __ A[i] > __max:
                __max A[i]

        __ _max >_ __max * 2:
            r.. _max_i

        r.. -1
