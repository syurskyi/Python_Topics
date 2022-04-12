____ h__ _______ heappop, heappush


c_ Solution:
    """
    @param: nums: an integer unsorted array
    @param: k: an integer from 1 to n
    @return: the kth largest element
    """
    ___ kthLargestElement2  nums, k
        __ n.. nums o. n.. k:
            r.. -1

        heap    # list
        ___ num __ nums:
            heappush(heap, num)

            __ l..(heap) > k:
                heappop(heap)

        r.. heappop(heap)
