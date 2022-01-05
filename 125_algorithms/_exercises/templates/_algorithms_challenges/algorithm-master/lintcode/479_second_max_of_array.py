c_ Solution:
    """
    @param: A: An integer array
    @return: The second max number in the array.
    """
    ___ secondMax  A):
        __ n.. A:
            r..

        max1 = max2 = float('-inf')
        ___ a __ A:
            __ a > max1:
                max2 = max1
                max1 = a
                _____
            __ a > max2:
                max2 = a

        r.. max2
