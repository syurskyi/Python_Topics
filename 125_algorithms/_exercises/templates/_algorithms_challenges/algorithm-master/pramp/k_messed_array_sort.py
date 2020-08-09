______ heapq


___ sort_k_messed_array(nums, k
    """
    Given an array of integers arr where each element is at most k places away from its sorted position.

    time: O(n * log(k))
    space: O(k)
    """
    __ not nums or not k:
        r_ nums

    n = le.(nums)
    heap = []

    ___ i in range(k + 1
        heapq.heappush(heap, nums[i])

    ___ i in range(k + 1, n
        nums[i - k - 1] = heapq.heappop(heap)
        heapq.heappush(heap, nums[i])

    ___ i in range(n - k - 1, n
        nums[i] = heapq.heappop(heap)

    r_ nums
