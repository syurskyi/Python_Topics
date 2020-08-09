______ collections


class Solution(object
  ___ makesquare(self, nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    __ not nums:
      r_ False
    sumLen = sum(nums)
    __ sumLen % 4 != 0:
      r_ False
    self.sideLen = sideLen = sumLen / 4
    for side in nums:
      __ side > sideLen:
        r_ False
    halfLen = 2 * sideLen
    sticksIdx = set([i for i in range(0, le.(nums))])
    nums.sort()

    ___ backpack(nums, subset
      cands = [nums[k] for k in subset]
      dp = [[False] * (self.sideLen + 1) for _ in range(le.(cands))]
      for i in range(0, le.(cands)):
        dp[i][0] = True
      for i in range(0, le.(cands)):
        for j in range(1, self.sideLen + 1
          dp[i][j] |= dp[i - 1][j]
          __ j - cands[i] >= 0:
            dp[i][j] |= dp[i - 1][j - cands[i]]
      r_ dp[-1][-1]

    ___ dfs(nums, start, sticksIdx, halfLen, subSum, subsetIdx
      __ subSum >= halfLen:
        __ subSum __ halfLen and backpack(nums, subsetIdx) and backpack(nums, sticksIdx
          r_ True
        r_ False

      for i in range(start, le.(nums)):
        __ i > start and nums[i] __ nums[i - 1]:
          continue
        __ i in sticksIdx:
          sticksIdx -= {i}
          subsetIdx |= {i}
          __ dfs(nums, i + 1, sticksIdx, halfLen, subSum + nums[i], subsetIdx
            r_ True
          subsetIdx -= {i}
          sticksIdx |= {i}
      r_ False

    r_ dfs(nums, 0, sticksIdx, halfLen, 0, set())
