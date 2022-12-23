c_ Solution o..
    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
    # def findUnsortedSubarray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     snums = nums[::]
    #     snums.sort()
    #     start = len(nums)
    #     end = 0
    #     for i in range(len(nums)):
    #         if snums[i] != nums[i]:
    #             start = min(start, i)
    #             end = max(end, i)
    #     if end >= start:
    #         return end - start + 1
    #     return 0

    ___ findUnsortedSubarray  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        stack =    # list
        l, r = l.. nums), 0
        ___ i __ r.. l.. nums)):
            w.. l.. stack) != 0 a.. nums[stack[-1]] > nums[i]:
                l = m.. l, stack.pop())
            stack.a.. i)
        stack =    # list
        ___ i __ r.. l.. nums) - 1, -1, -1
            w.. l.. stack) != 0 a.. nums[stack[-1]] < nums[i]:
                r = m..(r, stack.pop())
            stack.a.. i)
        __ r > l:
            r_ r - l + 1
        r_ 0

    # def findUnsortedSubarray(self, nums):
    #     smin = 2 ** 31 -1
    #     smax = -2 ** 31
    #     flag = False
    #     for i in range(1, len(nums)):
    #         if nums[i] < nums[i-1]:
    #             flag = True
    #         if flag:
    #             smin = min(smin, nums[i])
    #     flag = False
    #     for i in range(len(nums)-2, -1, -1):
    #         if nums[i] > nums[i+1]:
    #             flag = True
    #         if flag:
    #             smax = max(smax, nums[i])
    #     for l in range(len(nums)):
    #         if smin < nums[l]:
    #             break
    #     for r in range(len(nums)-1, -1, -1):
    #         if smax > nums[r]:
    #             break
    #     if r > l:
    #         return r - l + 1
    #     return 0
