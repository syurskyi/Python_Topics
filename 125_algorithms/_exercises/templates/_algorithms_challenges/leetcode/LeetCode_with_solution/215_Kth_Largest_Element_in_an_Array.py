c_ Solution o..
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     return sorted(nums, reverse=True)[k - 1]

    # def findKthLargest(self, nums, k):
    #     # build min heap
    #     heapq.heapify(nums)
    #     # remove n - k smallest number
    #     while len(nums) > k:
    #         heapq.heappop(nums)
    #     return nums[0]
    #     #return heapq.nlargest(k, nums)[-1]

    ___ findKthLargest  nums, k
        # shuffle nums to avoid n*n
        random.shuffle(nums)
        r_ quickSelection(nums, 0, l.. nums) - 1, l.. nums) - k)

    ___ quickSelection  nums, start, end, k
        __ start > end:
            r_ float('inf')
        pivot = nums[end]
        left = start
        ___ i __ r.. start, end
            __ nums[i] <= pivot:
                # swip left and i
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[end] = nums[end], nums[left]
        __ left __ k:
            r_ nums[left]
        ____ left < k:
            r_ quickSelection(nums, left + 1, end, k)
        ____
            r_ quickSelection(nums, start, left - 1, k)
