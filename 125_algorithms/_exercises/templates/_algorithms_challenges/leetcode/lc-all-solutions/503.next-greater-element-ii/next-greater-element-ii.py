class Solution(object):
  ___ nextGreaterElements(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [-1] * l..(nums)
    n = l..(nums)
    stack    # list
    nums *= 2
    ___ i, num __ e..(nums):
      w.... stack a.. nums[stack[-1]] < num:
        top = stack.pop()
        __ top < n:
          ans[top] = num
      stack.a..(i)
    r.. ans
