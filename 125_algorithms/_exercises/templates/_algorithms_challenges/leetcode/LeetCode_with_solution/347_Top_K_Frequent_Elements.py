c_ Solution o..
    ___ topKFrequent  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        r_ [k ___ k,v __ counter.most_common(k)]
        # return heapq.nlargest(k, count.keys(), key=count.get)
