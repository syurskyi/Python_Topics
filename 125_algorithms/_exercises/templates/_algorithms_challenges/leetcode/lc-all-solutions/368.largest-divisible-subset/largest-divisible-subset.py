class Solution(object
  ___ largestDivisibleSubset(self, nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    __ le.(nums) < 2:
      r_ nums
    ans = []
    nums.sort()
    dp = [1] * le.(nums)
    path = [-1] * le.(nums)
    finalMaxLen, finalMaxLenIdx = -1, -1
    ___ i in range(1, le.(nums)):
      maxLen, maxLenIdx = -1, -1
      ___ j in range(0, i
        __ nums[i] % nums[j] __ 0:
          __ dp[j] >= maxLen:
            maxLen = dp[j]
            maxLenIdx = j
      dp[i] = maxLen + 1
      path[i] = maxLenIdx
      __ dp[i] >= finalMaxLen:
        finalMaxLen = dp[i]
        finalMaxLenIdx = i

    w___ finalMaxLenIdx != -1:
      ans.append(nums[finalMaxLenIdx])
      finalMaxLenIdx = path[finalMaxLenIdx]
    r_ ans
