c_ Solution:
    # def searchInsert(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     min, pos = 0, 0
    #     max = len(nums) - 1
    #     while min <= max:
    #         # binary search
    #         pos = (max + min) / 2
    #         if nums[pos] == target:
    #             return pos
    #         elif nums[pos] > target:
    #             max = pos - 1
    #         else:
    #             min = pos + 1
    #     if min > pos:
    #         # this means that target is great than pos, and target
    #         # is not in nums
    #         return pos + 1
    #     return pos

    ___ searchInsert  nums, target):
        l, r = i..(0), l.. nums) - 1
        w.. l < r:
            mid = i..((l + r) / 2)
            __ nums[mid] < target:
                l = mid + 1
            ____
                r = mid
        __ nums[l] < target:
            r_ l + 1
        r_ l

    
    
__ ____ __ ____
    # begin
    s  ?
    print (s.searchInsert([1,3,5,6],5))    
    
