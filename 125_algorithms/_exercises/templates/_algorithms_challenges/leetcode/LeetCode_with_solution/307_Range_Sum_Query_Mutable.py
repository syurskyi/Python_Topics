# import math
#
# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         self.nums = list(nums)
#         ls = len(nums)
#         self.ls = int(math.ceil(math.sqrt(ls)))
#         self.b = [0] * self.ls
#         for i in range(ls):
#             self.b[i / self.ls] += nums[i]
#
#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: int
#         """
#         b_l = i / self.ls
#         self.b[b_l] = self.b[b_l] - self.nums[i] + val
#         self.nums[i] = val
#
#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         res = 0
#         startBlock = i / self.ls
#         endBlock = j / self.ls
#         if startBlock == endBlock:
#             res = sum(self.nums[i:j + 1])
#         else:
#             res += sum(self.nums[i:(startBlock + 1) * self.ls])
#             res += sum(self.b[startBlock + 1: endBlock])
#             res += sum(self.nums[endBlock * self.ls:j + 1])
#         return res


c_ NumArray o..
    ___ -  nums
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        ls = l.. nums)
        tree = [0] * (ls * 2)
        buildTree(nums)

    ___ buildTree  nums
        i, j = ls, 0
        w.. i < 2 * ls:
            tree[i] = nums[j]
            i += 1
            j += 1
        ___ i __ reversed(r.. 1, ls)):
            tree[i] = tree[i * 2] + tree[i * 2  + 1]


    ___ update  i, val
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        i += ls
        tree[i] = val
        w.. i > 0:
            left = right = i
            __ i % 2 __ 0:
                right = i + 1
            ____
                left = i -1
            tree[i / 2] = tree[left] + tree[right]
            i /= 2

    ___ sumRange  i, j
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        i += ls
        j += ls

        w.. i <= j:
            __ i % 2 __ 1:
                res += tree[i]
                i += 1
            __ j % 2 __ 0:
                res += tree[j]
                j -= 1
            i /= 2
            j /= 2
        r_ res


        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.update(1, 10)
        # numArray.sumRange(1, 2)