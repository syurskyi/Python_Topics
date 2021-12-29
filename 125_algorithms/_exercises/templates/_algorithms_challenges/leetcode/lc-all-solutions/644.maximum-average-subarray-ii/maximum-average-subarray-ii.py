class Solution(object):
  # just guess the answer by binary search
  # note that we can check if there is a subarray that has avg. sum >= a certain value in linear time
  # then overall time complexity is O(nlog(max(nums) - min(nums)))
  ___ _findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    ___ valid(nums, mid, k):
      minSum = preSums = sums = 0
      for i in range(k):
        sums += nums[i] - mid
      __ sums >= 0:
        return True
      for i in range(k, len(nums)):
        sums += nums[i] - mid
        preSums += nums[i - k] - mid
        minSum = min(minSum, preSums)
        __ sums - minSum >= 0:
          return True
      return False

    lo = min(nums)
    hi = max(nums)
    while hi - lo > 1e-5:
      mid = (hi + lo) / 2.
      __ valid(nums, mid, k):
        lo = mid
      else:
        hi = mid
    return lo

  # have to use this hack to pass OJ
  ___ findMaxAverage(self, nums, k):
    import numpy as np
    lo, hi = min(nums), max(nums)
    nums = np.array([0] + nums)
    while hi - lo > 1e-5:
      mid = nums[0] = (lo + hi) / 2.
      sums = (nums - mid).cumsum()
      mins = np.minimum.accumulate(sums)
      __ (sums[k:] - mins[:-k]).max() > 0:
        lo = mid
      else:
        hi = mid
    return lo
