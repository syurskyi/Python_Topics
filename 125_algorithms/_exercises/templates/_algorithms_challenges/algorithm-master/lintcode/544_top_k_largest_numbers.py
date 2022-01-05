____ heapq _______ heappush, heappop


c_ Solution:
    """
    @param: nums: an integer array
    @param: k: An integer
    @return: the top k largest numbers in array
    """
    ___ topk  nums, k):
        """
        min heap (normal case in heapq, max heap needs to times -1)
        """
        __ n.. nums:
            r..

        ans    # list
        ___ num __ nums:
            heappush(ans, num)

            __ l..(ans) > k:
                heappop(ans)

        ans.s..(r.._T..

        r.. ans
