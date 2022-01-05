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

c_ Solution:
    ___ jump  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        __ n __ 1:
            r.. 0
        start = 1
        end = nums[0]  # `end` is nums[start - 1]
        res = 1  # At least one step if len(nums) > 1
        reached = F..
        w.... end < n - 1:
            res += 1
            max_end = end  # `end` for the next loop
            ___ i __ r..(start, end + 1):
                __ i + nums[i] > max_end:
                    max_end = i + nums[i]
                    reached = T..
            __ n.. reached:
                r.. -1
            reached = F..
            start = end + 1
            end = max_end
        r.. res


s = Solution()
a1 = [2, 3, 1, 1, 4]
a2 = [3, 2, 1, 0, 4]
print s.jump(a1)
print s.jump(a2)
