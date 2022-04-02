"""
Heap
"""
_______ heapq


c_ Solution:
    ___ findMedianSortedArrays  a, b
        """
        :type a: list
        :type b: list
        :rtype: float
        """
        heap    # list
        n = 0

        ___ nums __ (a, b
            __ n.. nums:
                _____

            n += l..(nums)
            heapq.heappush(heap, (nums[0], nums, 0))

        __ n __ 0:
            r.. 0.0

        num = 0
        ___ _ __ r..((n + 1) // 2
            num, nums, i = heapq.heappop(heap)

            i += 1
            __ i < l..(nums
                heapq.heappush(heap, (nums[i], nums, i))

        __ n & 1 __ 1:
            r.. num * 1.0

        _num = heapq.heappop(heap)[0]
        r.. (num + _num) / 2.0


"""
Decreasing Approaching
"""
c_ Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    ___ findMedianSortedArrays  A, B
        n = l..(A) + l..(B)

        median = find_kth(A, 0, B, 0, n // 2 + 1)
        __ n % 2 __ 1:
            r.. median

        _median = find_kth(A, 0, B, 0, n // 2)
        r.. (median + _median) / 2.0

    ___ find_kth  A, i, B, j, k
        """
        example: A: [1, 2, 3, 4, 5, 6]
                 B: [2, 3, 4, 5]

        m + n = 10, median is `(5th + 6th) / 2`
        the process below is to find the `6th`
        r1/ k = 6
            1  2 |3| 4  5  6
            2  3 |4| 5
            _a = _b = 2
            a = 3, b = 4
            a < b
        r2/ k = 3
           -1--2--3-|4| 5  6
           |2| 3  4  5
            _a = 3, _b = 0
            a = 4, b = 2
            a > b
        r3/ k = 2
           -1--2--3-|4| 5  6
           -2-|3| 4  5
            _a = 3, _b = 1
            a = 4, b = 3
            a > b
        r4/ k = 1
           -1--2--3-|4| 5  6
           -2--3-|4| 5
            since k == 1
            return min(4, 4) = `4`
        """
        __ i >= l..(A
            r.. B[j + k - 1]
        __ j >= l..(B
            r.. A[i + k - 1]
        __ k __ 1:
            r.. m..(A[i], B[j])

        _a = i + k // 2 - 1
        _b = j + k // 2 - 1
        a = A[_a] __ _a < l..(A) ____ f__('inf')
        b = B[_b] __ _b < l..(B) ____ f__('inf')

        __ a < b:
            r.. find_kth(A, i + k // 2, B, j, k - k // 2)
        ____:
            r.. find_kth(A, i, B, j + k // 2, k - k // 2)
