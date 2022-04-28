import collections


c_ Solution o..
    ___ repeatedNTimes  A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = collections.Counter(A)
        r_ counter.most_common(1)[0][0]


__ ____ __ ____
    s  ?
    print s.repeatedNTimes([1, 2, 3, 3])
    print s.repeatedNTimes([2, 1, 2, 5, 3, 2])
    print s.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4])
