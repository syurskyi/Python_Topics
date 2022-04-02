"""
Given an array of n integers where n > 1, nums, return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array
does not count as extra space for the purpose of space complexity analysis.)
"""

c_ Solution(o..
    ___ productExceptSelf  nums
        """
        :type nums: List[int]
        :rtype: List[int]

        Memory Limit Exceeded
        """
        __ n.. nums:
            r.. []
        ____ l..(nums) __ 1:
            r.. [1]
        ____ l..(nums) __ 2:
            r.. nums[::-1]
        ____:
            m = 1
            rest = nums[1:]
            ___ c __ rest:
                m *= c
            res = [m]
            ___ r __ productExceptSelf(rest
                res.a..(r * nums[0])
            r.. res


a1 = [1, 2, 3]
a2 = [2, 3, 4]
a3 = [1, 2, 3, 4]
a4 = [2, 3, 4, 5]

s = Solution()
print(s.productExceptSelf(a1))
print(s.productExceptSelf(a2))
print(s.productExceptSelf(a3))
print(s.productExceptSelf(a4))
