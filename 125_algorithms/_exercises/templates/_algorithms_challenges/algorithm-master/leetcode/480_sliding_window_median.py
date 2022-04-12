_______ h__


c_ HashHeapq:
    ___ -
        __heap    # list

    ___  -r
        r.. r.. (__heap)

    ___ __len__
        r.. l..(__heap)

    ___ __bool__
        r.. b..(__heap)

    ___ push  val
        h__.heappush(__heap, val)

    ___ pop
        __ n.. __heap:
            r..

        r.. h__.heappop(__heap)

    ___ remove  val
        __ n.. __heap:
            r..

        i 0
        n l..(__heap)

        w.... i < n a.. __heap[i] !_ val:
            i += 1

        __ i __ n:
            r..

        __ i __ n - 1:
            __heap.p.. )
        ____
            __heap[i] __heap[-1]
            __heap.p.. )
            h__._siftup(__heap, i)
            h__._siftdown(__heap, 0, i)

    ___ top
        __ n.. __heap:
            r..

        r.. __heap[0]


c_ Solution:
    ___ medianSlidingWindow  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        ans    # list

        __ n.. nums o. k <_ 0 o. l..(nums) < k:
            r.. ans

        minheap HashHeapq()
        maxheap HashHeapq()

        ___ i __ r..(l..(nums:
            # remove nums[i - k]
            __ i >_ k:
                __ minheap a.. nums[i - k] >_ minheap.top
                    minheap.remove(nums[i - k])
                ____
                    maxheap.remove(- nums[i - k])

            # add nums[i]
            __ minheap a.. nums[i] >_ minheap.top
                minheap.push(nums[i])
            ____
                maxheap.push(- nums[i])

            # get median
            __ i >_ k - 1:
                ans.a..(get_median

        r.. ans

    ___ get_median
        __ n.. minheap a.. n.. maxheap:
            r.. 0.0

        w.... l..(minheap) > l..(maxheap) + 1:
            maxheap.push(- minheap.pop

        w.... l..(maxheap) > l..(minheap
            minheap.push(- maxheap.pop

        __ l..(minheap) > l..(maxheap
            r.. minheap.top() * 1.0

        r.. (minheap.top() - maxheap.top / 2.0
