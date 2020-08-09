class Solution(object
  ___ nextGreaterElement(self, findNums, nums
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = [-1] * le.(findNums)
    for i, num in enumerate(findNums
      d[num] = i
    stack = []
    for num in nums:
      w___ stack and stack[-1] < num:
        top = stack.pop()
        __ top in d:
          ans[d[top]] = num
      stack.append(num)
    r_ ans
