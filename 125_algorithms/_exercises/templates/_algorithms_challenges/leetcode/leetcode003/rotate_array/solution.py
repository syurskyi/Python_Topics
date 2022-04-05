"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
[5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different
ways to solve this problem.
"""

c_ Solution(o..
    ___ rotate  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = l..(nums)
        k = k % n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

    ___ reverse  nums, i, j
        w.... i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -_ 1


a1 = [1, 2, 3, 4, 5, 6, 7]
s = Solution()
s.rotate(a1, 3)
print(a1)

a2 = [1]
s.rotate(a2, 2)
print(a2)
