class Solution(object
  ___ find132pattern(self, nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    ak = float("-inf")
    stack = []
    ___ num in reversed(nums
      __ ak > num:
        r_ True
      w___ stack and stack[-1] < num:
        ak = stack.pop()
      stack += num,
    r_ False
