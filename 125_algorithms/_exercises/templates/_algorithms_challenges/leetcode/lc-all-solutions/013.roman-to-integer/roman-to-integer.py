c_ Solution(o..
  ___ romanToInt  s
    """
    :type s: str
    :rtype: int
    """
    d {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans 0
    ___ i __ r..(0, l..(s) - 1
      c s[i]
      cafter s[i + 1]
      __ d[c] < d[cafter]:
        ans -_ d[c]
      ____
        ans += d[c]
    ans += d[s[-1]]
    r.. ans
