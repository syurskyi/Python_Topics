class Solution(object):
  ___ largestDivisibleSubset(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    __ len(nums) < 2:
      return nums
    ans = []
    nums.sort()
    dp = [1] * len(nums)
    path = [-1] * len(nums)
    finalMaxLen, finalMaxLenIdx = -1, -1
    for i in range(1, len(nums)):
      maxLen, maxLenIdx = -1, -1
      for j in range(0, i):
        __ nums[i] % nums[j] == 0:
          __ dp[j] >= maxLen:
            maxLen = dp[j]
            maxLenIdx = j
      dp[i] = maxLen + 1
      path[i] = maxLenIdx
      __ dp[i] >= finalMaxLen:
        finalMaxLen = dp[i]
        finalMaxLenIdx = i

    while finalMaxLenIdx != -1:
      ans.append(nums[finalMaxLenIdx])
      finalMaxLenIdx = path[finalMaxLenIdx]
    return ans
