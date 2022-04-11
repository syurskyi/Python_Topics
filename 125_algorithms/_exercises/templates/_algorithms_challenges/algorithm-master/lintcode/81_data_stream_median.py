_______ heapq


c_ Solution:
    ___ medianII  nums
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        ans    # list
        __ n.. nums:
            r.. ans

        minheap    # list
        maxheap    # list
        median 0

        ___ num __ nums:
            __ num < median:
                heapq.heappush(maxheap, -num)
            ____
                heapq.heappush(minheap, num)

            w.... l..(minheap) > l..(maxheap
                heapq.heappush(maxheap, -heapq.heappop(minheap

            w.... l..(maxheap) > l..(minheap) + 1:
                heapq.heappush(minheap, -heapq.heappop(maxheap

            __ maxheap:
                median -maxheap[0]
            ____
                median 0

            ans.a..(median)

        r.. ans
