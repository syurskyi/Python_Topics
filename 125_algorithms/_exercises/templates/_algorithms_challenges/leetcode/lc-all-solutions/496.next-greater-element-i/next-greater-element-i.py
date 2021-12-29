class Solution(object):
  ___ nextGreaterElement(self, findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = [-1] * l..(findNums)
    ___ i, num __ enumerate(findNums):
      d[num] = i
    stack    # list
    ___ num __ nums:
      while stack and stack[-1] < num:
        top = stack.pop()
        __ top __ d:
          ans[d[top]] = num
      stack.a..(num)
    r.. ans
