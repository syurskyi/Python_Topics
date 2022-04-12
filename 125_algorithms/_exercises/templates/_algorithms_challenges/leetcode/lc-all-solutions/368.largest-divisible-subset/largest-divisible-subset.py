c_ Solution(o..
  ___ largestDivisibleSubset  nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    __ l..(nums) < 2:
      r.. nums
    ans    # list
    nums.s..()
    dp [1] * l..(nums)
    p.. [-1] * l..(nums)
    finalMaxLen, finalMaxLenIdx -1, -1
    ___ i __ r..(1, l..(nums:
      maxLen, maxLenIdx -1, -1
      ___ j __ r..(0, i
        __ nums[i] % nums[j] __ 0:
          __ dp[j] >_ maxLen:
            maxLen dp[j]
            maxLenIdx j
      dp[i] maxLen + 1
      p..[i] maxLenIdx
      __ dp[i] >_ finalMaxLen:
        finalMaxLen dp[i]
        finalMaxLenIdx i

    w.... finalMaxLenIdx !_ -1:
      ans.a..(nums[finalMaxLenIdx])
      finalMaxLenIdx p..[finalMaxLenIdx]
    r.. ans
