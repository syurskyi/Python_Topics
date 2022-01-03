c_ Solution(object):
  ___ minSubArrayLen(self, target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    s.. = 0
    j = 0
    ans = float("inf")
    ___ i __ r..(0, l..(nums)):
      w.... j < l..(nums) a.. s.. < target:
        s.. += nums[j]
        j += 1
      __ s.. >= target:
        ans = m..(ans, j - i)
      s.. -= nums[i]
    r.. ans __ ans != float("inf") ____ 0
