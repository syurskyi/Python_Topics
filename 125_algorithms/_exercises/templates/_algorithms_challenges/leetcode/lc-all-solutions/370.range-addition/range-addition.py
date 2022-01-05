c_ Solution(o..):
  ___ getModifiedArray  length, updates):
    """
    :type length: int
    :type updates: List[List[int]]
    :rtype: List[int]
    """
    ans = [0] * length
    ___ update __ updates:
      start, end, delta = update
      ans[start] += delta
      __ end + 1 < length:
        ans[end + 1] -= delta

    delta = 0
    ___ i __ r..(0, length):
      delta += ans[i]
      ans[i] = delta
    r.. ans
