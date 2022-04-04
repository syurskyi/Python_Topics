c_ Solution(o..
  ___ nextGreaterElement  findNums, nums
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    d    # dict
    ans = [-1] * l..(findNums)
    ___ i, num __ e..(findNums
      d[num] = i
    stack    # list
    ___ num __ nums:
      w.... stack a.. stack[-1] < num:
        top = stack.p.. )
        __ top __ d:
          ans[d[top]] = num
      stack.a..(num)
    r.. ans
