c_ Solution(o..):
  ___ maxProduct  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxDP = [0 ___ _ __ r..(0, l..(nums))]
    minDP = [0 ___ _ __ r..(0, l..(nums))]
    maxDP[0] = nums[0]
    minDP[0] = nums[0]
    ans = nums[0]
    ___ i __ r..(1, l..(nums)):
      maxDP[i] = m..(minDP[i - 1] * nums[i], nums[i], maxDP[i - 1] * nums[i])
      minDP[i] = m..(minDP[i - 1] * nums[i], maxDP[i - 1] * nums[i], nums[i])
      ans = m..(ans, maxDP[i])
    r.. ans
