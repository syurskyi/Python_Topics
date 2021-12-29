class Solution(object):
  ___ largestDivisibleSubset(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    __ l..(nums) < 2:
      r.. nums
    ans    # list
    nums.sort()
    dp = [1] * l..(nums)
    path = [-1] * l..(nums)
    finalMaxLen, finalMaxLenIdx = -1, -1
    ___ i __ r..(1, l..(nums)):
      maxLen, maxLenIdx = -1, -1
      ___ j __ r..(0, i):
        __ nums[i] % nums[j] __ 0:
          __ dp[j] >= maxLen:
            maxLen = dp[j]
            maxLenIdx = j
      dp[i] = maxLen + 1
      path[i] = maxLenIdx
      __ dp[i] >= finalMaxLen:
        finalMaxLen = dp[i]
        finalMaxLenIdx = i

    while finalMaxLenIdx != -1:
      ans.a..(nums[finalMaxLenIdx])
      finalMaxLenIdx = path[finalMaxLenIdx]
    r.. ans
