class Solution(object
  ___ magicalString(self, n
    """
    :type n: int
    :rtype: int
    """
    s = "122"
    p = 2
    w___ le.(s) < n:
      s += str((3 - int(s[-1]))) * int(s[p])
      p += 1
    r_ s[:n].count("1")
