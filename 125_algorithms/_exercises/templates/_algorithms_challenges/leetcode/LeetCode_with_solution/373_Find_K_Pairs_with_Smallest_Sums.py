c_ Solution o..
    ___ kSmallestPairs  nums1, nums2, k
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # https://discuss.leetcode.com/topic/50450/slow-1-liner-to-fast-solutions
        queue =    # list
        ___ push(i, j
            __ i < l.. nums1) a.. j < l.. nums2
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs =    # list
        w.. queue a.. l.. pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.a.. [nums1[i], nums2[j]])
            push(i, j + 1)
            __ j __ 0:
                push(i + 1, 0)
        r_ pairs