from random import randint


class Solution:
    ___ __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A

    ___ pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = -1
        cnt = 0

        for i in range(len(self.A)):
            __ self.A[i] != target:
                continue
            cnt += 1
            __ randint(1, cnt) == cnt:
                res = i

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
