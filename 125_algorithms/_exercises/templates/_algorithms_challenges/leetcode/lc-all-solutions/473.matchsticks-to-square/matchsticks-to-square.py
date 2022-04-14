_______ c..


c_ Solution(o..
  ___ makesquare  nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    __ n.. nums:
      r.. F..
    sumLen s..(nums)
    __ sumLen % 4 !_ 0:
      r.. F..
    sideLen sideLen sumLen / 4
    ___ side __ nums:
      __ side > sideLen:
        r.. F..
    halfLen 2 * sideLen
    sticksIdx s..( i ___ ? __ r..(0, l..(nums])
    nums.s..()

    ___ backpack(nums, subset
      cands [nums[k] ___ k __ subset]
      dp [[F..] * (sideLen + 1) ___ _ __ r..(l..(cands]
      ___ i __ r..(0, l..(cands:
        dp[i][0] T..
      ___ i __ r..(0, l..(cands:
        ___ j __ r..(1, sideLen + 1
          dp[i][j] |= dp[i - 1][j]
          __ j - cands[i] >_ 0:
            dp[i][j] |= dp[i - 1][j - cands[i]]
      r.. dp[-1][-1]

    ___ dfs(nums, start, sticksIdx, halfLen, subSum, subsetIdx
      __ subSum >_ halfLen:
        __ subSum __ halfLen a.. backpack(nums, subsetIdx) a.. backpack(nums, sticksIdx
          r.. T..
        r.. F..

      ___ i __ r..(start, l..(nums:
        __ i > start a.. nums[i] __ nums[i - 1]:
          _____
        __ i __ sticksIdx:
          sticksIdx -_ {i}
          subsetIdx |= {i}
          __ dfs(nums, i + 1, sticksIdx, halfLen, subSum + nums[i], subsetIdx
            r.. T..
          subsetIdx -_ {i}
          sticksIdx |= {i}
      r.. F..

    r.. dfs(nums, 0, sticksIdx, halfLen, 0, s..
