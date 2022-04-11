c_ Solution(o..
  ___ minSubArrayLen  target, nums
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    s.. 0
    j 0
    ans f__("inf")
    ___ i __ r..(0, l..(nums:
      w.... j < l..(nums) a.. s.. < target:
        s.. += nums[j]
        j += 1
      __ s.. >_ target:
        ans m..(ans, j - i)
      s.. -_ nums[i]
    r.. ans __ ans != f__("inf") ____ 0
