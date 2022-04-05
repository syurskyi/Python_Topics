_______ heapq


c_ HashHeapqWithLazy:
    ___ -
        __heap    # list
        __deleted    # dict
        __size = 0

    ___ __len__
        r.. __size

    ___ __bool__
        r.. __size > 0

    ___ push  val
        heapq.heappush(__heap, val)
        __size += 1

    ___ pop
        __ _is_empty
            r..

        __size -_ 1
        r.. heapq.heappop(__heap)

    ___ remove  val
        __ _is_empty
            r..

        __size -_ 1
        __deleted[val] = __deleted.g.. val, 0) + 1

    ___ top
        __ _is_empty
            r..

        r.. __heap[0]

    ___ _is_empty
        w.... __heap a.. __deleted.g.. __heap[0]
            val = heapq.heappop(__heap)
            __deleted[val] -_ 1

        r.. __size __ 0


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

        minheap = HashHeapqWithLazy()
        maxheap = HashHeapqWithLazy()

        ___ i __ r..(l..(nums:
            # remove nums[i - k]
            __ i >_ k:
                __ minheap a.. nums[i - k] >_ minheap.top
                    minheap.remove(nums[i - k])
                ____
                    maxheap.remove(-1 * nums[i - k])

            # add nums[i]
            __ minheap a.. nums[i] >_ minheap.top
                minheap.push(nums[i])
            ____
                maxheap.push(-1 * nums[i])

            # get median
            __ i >_ k - 1:
                ans.a..(get_median

        r.. ans

    ___ get_median
        __ n.. maxheap a.. n.. minheap:
            r.. 0

        w.... l..(maxheap) > l..(minheap) + 1:
            minheap.push(-1 * maxheap.pop

        w.... l..(minheap) > l..(maxheap
            maxheap.push(-1 * minheap.pop

        r.. -1 * maxheap.top()
