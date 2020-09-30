class Solution(object
  ___ checkSubarraySum(self, nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    __ k __ 0:
      r_ "0,0" __ ",".join([str(n) ___ n __ nums])
    __ le.(nums) < 2:
      r_ False
    __ le.(nums) __ 2:
      r_ su.(nums) % k __ 0
    ppSum = 0
    subSum = nums[0] + nums[1]
    d = set([0])
    ___ i __ range(2, le.(nums)):
      ppSum = (ppSum + nums[i - 2]) % k
      d |= {ppSum}
      subSum = (subSum + nums[i]) % k
      __ subSum % k __ d:
        r_ True
    r_ False
