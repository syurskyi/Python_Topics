class Solution(object
  ___ nextGreaterElements(self, nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [-1] * le.(nums)
    n = le.(nums)
    stack = []
    nums *= 2
    ___ i, num in enumerate(nums
      w___ stack and nums[stack[-1]] < num:
        top = stack.p..
        __ top < n:
          ans[top] = num
      stack.append(i)
    r_ ans
