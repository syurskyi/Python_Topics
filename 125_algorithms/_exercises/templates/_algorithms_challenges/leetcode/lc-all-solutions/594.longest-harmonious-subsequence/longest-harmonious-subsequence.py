c_ Solution(o..):
  ___ findLHS  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    d = c...Counter(nums)
    ___ num __ nums:
      __ num + 1 __ d:
        ans = m..(ans, d[num] + d[num + 1])
    r.. ans
