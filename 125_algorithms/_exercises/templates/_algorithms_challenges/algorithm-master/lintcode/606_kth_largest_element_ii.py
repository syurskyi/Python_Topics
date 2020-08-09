from heapq ______ heappop, heappush


class Solution:
    """
    @param: nums: an integer unsorted array
    @param: k: an integer from 1 to n
    @return: the kth largest element
    """
    ___ kthLargestElement2(self, nums, k
        __ not nums or not k:
            r_ -1

        heap = []
        ___ num in nums:
            heappush(heap, num)

            __ le.(heap) > k:
                heappop(heap)

        r_ heappop(heap)
