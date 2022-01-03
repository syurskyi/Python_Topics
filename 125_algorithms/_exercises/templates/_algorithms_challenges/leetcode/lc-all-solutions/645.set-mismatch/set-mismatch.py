c_ Solution(object):
  ___ findErrorNums(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [-1, -1]
    diff = diffSquare = 0
    ___ i, num __ e..(nums):
      diff += i + 1 - num
      diffSquare += (i + 1) ** 2 - num ** 2
    ans[1] = (diffSquare / diff + diff) / 2
    ans[0] = ans[1] - diff
    ans.s..()
    __ diff > 0:
      r.. ans
    r.. ans[::-1]
