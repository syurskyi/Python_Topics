c_ Solution(o..):
  ___ checkSubarraySum  nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    __ k __ 0:
      r.. "0,0" __ ",".j..([s..(n) ___ n __ nums])
    __ l..(nums) < 2:
      r.. F..
    __ l..(nums) __ 2:
      r.. s..(nums) % k __ 0
    ppSum = 0
    subSum = nums[0] + nums[1]
    d = set([0])
    ___ i __ r..(2, l..(nums)):
      ppSum = (ppSum + nums[i - 2]) % k
      d |= {ppSum}
      subSum = (subSum + nums[i]) % k
      __ subSum % k __ d:
        r.. T..
    r.. F..
