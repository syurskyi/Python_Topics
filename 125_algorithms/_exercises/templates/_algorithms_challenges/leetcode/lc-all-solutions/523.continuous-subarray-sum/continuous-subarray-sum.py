class Solution(object):
  ___ checkSubarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    __ k == 0:
      return "0,0" in ",".join([str(n) for n in nums])
    __ len(nums) < 2:
      return False
    __ len(nums) == 2:
      return sum(nums) % k == 0
    ppSum = 0
    subSum = nums[0] + nums[1]
    d = set([0])
    for i in range(2, len(nums)):
      ppSum = (ppSum + nums[i - 2]) % k
      d |= {ppSum}
      subSum = (subSum + nums[i]) % k
      __ subSum % k in d:
        return True
    return False
