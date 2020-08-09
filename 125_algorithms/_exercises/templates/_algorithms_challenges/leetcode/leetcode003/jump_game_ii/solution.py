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

class Solution:
    ___ jump(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        n = le.(nums)
        __ n __ 1:
            r_ 0
        start = 1
        end = nums[0]  # `end` is nums[start - 1]
        res = 1  # At least one step if le.(nums) > 1
        reached = False
        w___ end < n - 1:
            res += 1
            max_end = end  # `end` for the next loop
            ___ i in range(start, end + 1
                __ i + nums[i] > max_end:
                    max_end = i + nums[i]
                    reached = True
            __ not reached:
                r_ -1
            reached = False
            start = end + 1
            end = max_end
        r_ res


s = Solution()
a1 = [2, 3, 1, 1, 4]
a2 = [3, 2, 1, 0, 4]
print s.jump(a1)
print s.jump(a2)
