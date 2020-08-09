class Solution(object
  ___ rotate(self, nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    __ le.(nums) __ 0 or k __ 0:
      r_

    ___ reverse(start, end, s
      w___ start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    n = le.(nums) - 1
    k = k % le.(nums)
    reverse(0, n - k, nums)
    reverse(n - k + 1, n, nums)
    reverse(0, n, nums)
