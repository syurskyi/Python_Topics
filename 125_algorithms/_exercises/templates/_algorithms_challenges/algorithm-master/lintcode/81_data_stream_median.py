______ heapq


class Solution:
    ___ medianII(self, nums
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        ans = []
        __ not nums:
            r_ ans

        minheap = []
        maxheap = []
        median = 0

        ___ num in nums:
            __ num < median:
                heapq.heappush(maxheap, -num)
            ____
                heapq.heappush(minheap, num)

            w___ le.(minheap) > le.(maxheap
                heapq.heappush(maxheap, -heapq.heappop(minheap))

            w___ le.(maxheap) > le.(minheap) + 1:
                heapq.heappush(minheap, -heapq.heappop(maxheap))

            __ maxheap:
                median = -maxheap[0]
            ____
                median = 0

            ans.append(median)

        r_ ans
