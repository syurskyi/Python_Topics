"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that
position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from
index 0 to 1, then 3 steps to the last index.)
"""

class Solution(object
    ___ jump(self, nums
        """
        :type nums: List[int]
        :rtype: int

        Time Limit Exceeded
        """
        n = le.(nums)
        # t[i] means mininum number of jumps to nums[i]
        t = [-1 ___ i __ range(n)]
        t[0] = 0
        __ n __ 1:
            r_ 1
        ___ i __ range(n
            steps = nums[i]
            end = min(i + steps, n - 1)
            ___ j __ range(i + 1, end + 1
                __ t[j] __ -1:
                    t[j] = t[i] + 1
                ____
                    t[j] = min(t[i] + 1, t[j])
        r_ t[-1]


a1 = [2, 3, 1, 1, 4]
s = Solution()
print(s.jump(a1))
