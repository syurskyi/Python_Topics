import heapq


class Solution:
    ___ medianII(self, nums):
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        ans = []
        __ not nums:
            return ans

        minheap = []
        maxheap = []
        median = 0

        for num in nums:
            __ num < median:
                heapq.heappush(maxheap, -num)
            else:
                heapq.heappush(minheap, num)

            while len(minheap) > len(maxheap):
                heapq.heappush(maxheap, -heapq.heappop(minheap))

            while len(maxheap) > len(minheap) + 1:
                heapq.heappush(minheap, -heapq.heappop(maxheap))

            __ maxheap:
                median = -maxheap[0]
            else:
                median = 0

            ans.append(median)

        return ans
