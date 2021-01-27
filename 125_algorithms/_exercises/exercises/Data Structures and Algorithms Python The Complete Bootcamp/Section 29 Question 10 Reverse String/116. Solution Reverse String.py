class Solution:
    ___ reverseString  s):
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = le.(s) - 1

        w__ left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1