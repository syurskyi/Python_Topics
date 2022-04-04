c_ Solution(o..
  ___ candy  ratings
    """
    :type ratings: List[int]
    :rtype: int
    """
    n = l..(ratings)
    left = [1] * n
    ans = 0
    ___ i __ r..(1, n
      __ ratings[i] > ratings[i - 1]:
        left[i] = left[i - 1] + 1
    ans = left[-1]
    ___ i __ r..(r..(0, n - 1:
      __ ratings[i] > ratings[i + 1]:
        left[i] = m..(left[i], left[i + 1] + 1)
      ans += left[i]
    r.. ans
