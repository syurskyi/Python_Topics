_______ collections


class Solution(object):
  ___ makesquare(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    __ n.. nums:
      r.. False
    sumLen = s..(nums)
    __ sumLen % 4 != 0:
      r.. False
    self.sideLen = sideLen = sumLen / 4
    ___ side __ nums:
      __ side > sideLen:
        r.. False
    halfLen = 2 * sideLen
    sticksIdx = set([i ___ i __ r..(0, l..(nums))])
    nums.s..()

    ___ backpack(nums, subset):
      cands = [nums[k] ___ k __ subset]
      dp = [[False] * (self.sideLen + 1) ___ _ __ r..(l..(cands))]
      ___ i __ r..(0, l..(cands)):
        dp[i][0] = True
      ___ i __ r..(0, l..(cands)):
        ___ j __ r..(1, self.sideLen + 1):
          dp[i][j] |= dp[i - 1][j]
          __ j - cands[i] >= 0:
            dp[i][j] |= dp[i - 1][j - cands[i]]
      r.. dp[-1][-1]

    ___ dfs(nums, start, sticksIdx, halfLen, subSum, subsetIdx):
      __ subSum >= halfLen:
        __ subSum __ halfLen a.. backpack(nums, subsetIdx) a.. backpack(nums, sticksIdx):
          r.. True
        r.. False

      ___ i __ r..(start, l..(nums)):
        __ i > start a.. nums[i] __ nums[i - 1]:
          continue
        __ i __ sticksIdx:
          sticksIdx -= {i}
          subsetIdx |= {i}
          __ dfs(nums, i + 1, sticksIdx, halfLen, subSum + nums[i], subsetIdx):
            r.. True
          subsetIdx -= {i}
          sticksIdx |= {i}
      r.. False

    r.. dfs(nums, 0, sticksIdx, halfLen, 0, set())
