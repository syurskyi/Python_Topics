"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

c_ Solution(o..
    ___ findMin  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        left = 0
        right = n - 1
        __ n __ 1 o. nums[left] < nums[right]:
            r.. nums[0]
        w.... left <= right:
            mid = left + (right - left) / 2
            __ mid > 0 a.. nums[mid - 1] > nums[mid]:
                r.. nums[mid]
            # The minimum element is in the right side
            ____ nums[mid] > nums[right]:
                left = mid + 1
            # The minimum element is in the left side
            ____:
                right = mid - 1


a1 = [4, 5, 6, 7, 0, 1, 2]
s = Solution()
print(s.findMin(a1))
