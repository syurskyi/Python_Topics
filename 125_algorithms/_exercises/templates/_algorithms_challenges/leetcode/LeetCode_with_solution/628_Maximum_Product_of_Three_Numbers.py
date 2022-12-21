c_ Solution o..
    # def maximumProduct(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     nums.sort()
    #     # Check min1*min2*max1 and max1*max2*max3
    #     return max(reduce(lambda x, y: x * y, nums[:2]) * nums[-1],
    #                reduce(lambda x, y: x * y, nums[-3:]))

    ___ maximumProduct  nums
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')
        ___ num __ nums:
            __ num <= min1:
                min2 = min1
                min1 = num
            ____ num <= min2:
                min2 = num
            __ num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            ____ num >= max2:
                max3 = max2
                max2 = num
            ____ num >= max3:
                max3 = num
        r_ m..(min1 * min2 * max1, max1 * max2 * max3)
