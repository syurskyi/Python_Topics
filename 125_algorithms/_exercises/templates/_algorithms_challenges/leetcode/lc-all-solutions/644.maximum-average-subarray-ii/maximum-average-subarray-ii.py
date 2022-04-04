c_ Solution(o..
  # just guess the answer by binary search
  # note that we can check if there is a subarray that has avg. sum >= a certain value in linear time
  # then overall time complexity is O(nlog(max(nums) - min(nums)))
  ___ _findMaxAverage  nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    ___ valid(nums, mid, k
      minSum = preSums = sums = 0
      ___ i __ r..(k
        sums += nums[i] - mid
      __ sums >_ 0:
        r.. T..
      ___ i __ r..(k, l..(nums:
        sums += nums[i] - mid
        preSums += nums[i - k] - mid
        minSum = m..(minSum, preSums)
        __ sums - minSum >_ 0:
          r.. T..
      r.. F..

    lo = m..(nums)
    hi = m..(nums)
    w.... hi - lo > 1e-5:
      mid = (hi + lo) / 2.
      __ valid(nums, mid, k
        lo = mid
      ____
        hi = mid
    r.. lo

  # have to use this hack to pass OJ
  ___ findMaxAverage  nums, k
    _______ numpy __ np
    lo, hi = m..(nums), m..(nums)
    nums = np.array([0] + nums)
    w.... hi - lo > 1e-5:
      mid = nums[0] = (lo + hi) / 2.
      sums = (nums - mid).cumsum()
      mins = np.minimum.accumulate(sums)
      __ (sums[k:] - mins[:-k]).m..() > 0:
        lo = mid
      ____
        hi = mid
    r.. lo
