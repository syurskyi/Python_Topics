from heapq import heappop, heappush


class Solution:
    """
    @param: nums: an integer unsorted array
    @param: k: an integer from 1 to n
    @return: the kth largest element
    """
    ___ kthLargestElement2(self, nums, k):
        __ not nums or not k:
            return -1

        heap = []
        for num in nums:
            heappush(heap, num)

            __ len(heap) > k:
                heappop(heap)

        return heappop(heap)
