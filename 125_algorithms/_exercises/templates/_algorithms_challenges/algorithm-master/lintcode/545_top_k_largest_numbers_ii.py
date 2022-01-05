____ heapq _______ heappop, heappush


c_ Solution:
    """
    @param: k: An integer
    """
    ___ - , k):
        k = k
        tops    # list

    """
    @param: num: Number to be added
    @return: nothing
    """
    ___ add  num):
        # push in first, since we cannot ensure
        # the incoming num will stay in tops
        heappush(tops, num)

        __ l..(tops) > k:
            heappop(tops)

    """
    @return: Top k element
    """
    ___ topk
        r.. s..(tops, r.._T..
