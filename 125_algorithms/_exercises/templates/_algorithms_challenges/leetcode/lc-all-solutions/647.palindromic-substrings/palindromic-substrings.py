c_ Solution(o..
  ___ countSubstrings  s
    """
    :type s: str
    :rtype: int
    """
    n = l..(s)
    ans = 0
    ___ i __ r..(n
      left = right = i
      w.... left >_ 0 a.. right < n a.. s[left] __ s[right]:
        ans += 1
        left -_ 1
        right += 1

      left = i
      right = i + 1
      w.... left >_ 0 a.. right < n a.. s[left] __ s[right]:
        ans += 1
        left -_ 1
        right += 1
    r.. ans
