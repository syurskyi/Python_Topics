_______ h__


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
                h__.heappush(maxheap, -num)
            ____
                h__.heappush(minheap, num)

            w.... l..(minheap) > l..(maxheap
                h__.heappush(maxheap, -h__.heappop(minheap

            w.... l..(maxheap) > l..(minheap) + 1:
                h__.heappush(minheap, -h__.heappop(maxheap

            __ maxheap:
                median -maxheap[0]
            ____
                median 0

            ans.a..(median)

        r.. ans
