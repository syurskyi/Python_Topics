c_ Solution(o..
  ___ subarraySum  nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    preSum = ans = 0
    visit = {0: 1}
    ___ i, n __ e..(nums
      preSum += n
      ans += visit.g.. preSum - k, 0)
      visit[preSum] = visit.g.. preSum, 0) + 1
    r.. ans
