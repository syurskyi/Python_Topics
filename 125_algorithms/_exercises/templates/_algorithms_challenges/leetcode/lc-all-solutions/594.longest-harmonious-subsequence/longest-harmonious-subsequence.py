c_ Solution(object):
  ___ findLHS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    d = c...Counter(nums)
    ___ num __ nums:
      __ num + 1 __ d:
        ans = max(ans, d[num] + d[num + 1])
    r.. ans
