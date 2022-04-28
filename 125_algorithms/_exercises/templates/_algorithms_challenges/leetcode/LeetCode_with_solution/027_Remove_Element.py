# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
c_ Solution o..
    # def removeElement(self, nums, val):
    #     ls = len(nums)
    #     if ls == 0:
    #         return ls
    #     pos = 0
    #     for i in range(ls):
    #         if nums[i] == val:
    #             continue
    #         else:
    #             nums[pos] = nums[i]
    #             pos += 1
    #     # del nums[pos:]
    #     return pos

    ___ removeElement  nums, val):
        ls = l.. nums)
        __ ls __ 0:
            r_ ls
        count = 0
        index = 0
        w.. index < ls - count:
            __ nums[index] __ val:
                nums[index] = nums[ls - 1 - count]
                count += 1
            ____
                index += 1
        r_ ls - count

__ ____ __ ____
    # begin
    s  ?
    print s.removeElement([1], 1)

