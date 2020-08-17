class Solution(object
  ___ nextGreaterElement(self, findNums, nums
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = [-1] * le.(findNums)
    ___ i, num in enumerate(findNums
      d[num] = i
    stack = []
    ___ num in nums:
      w___ stack and stack[-1] < num:
        top = stack.p..
        __ top in d:
          ans[d[top]] = num
      stack.append(num)
    r_ ans
