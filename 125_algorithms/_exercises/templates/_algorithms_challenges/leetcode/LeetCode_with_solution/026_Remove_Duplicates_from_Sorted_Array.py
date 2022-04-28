c_ Solution o..
    # def removeDuplicates(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #     ls = len(nums)
    #     if ls <= 1:
    #         return ls
    #     last = nums[0]
    #     pos = 1
    #     for t in nums[1:]:
    #         if t == last:
    #             continue
    #         else:
    #             nums[pos] = t
    #             pos += 1
    #             last = t
    #     return pos

    # https://leetcode.com/articles/remove-duplicates-sorted-array/
    ___ removeDuplicates  nums):
        __ l.. nums) __ 0:
            r_ 0
        left = 0
        ___ i __ r.. 1, l.. nums)):
            __ nums[left] __ nums[i]:
                continue
            ____
                left += 1
                nums[left] = nums[i]
        r_ left + 1

