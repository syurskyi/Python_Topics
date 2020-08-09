class Solution(object
  ___ checkRecord(self, s
    """
    :type s: str
    :rtype: bool
    """
    a = l = 0
    ___ c in s:
      __ c __ "L":
        l += 1
      ____ c __ "A":
        a += 1
        l = 0
      ____
        l = 0
      __ a > 1 or l > 2:
        r_ False
    r_ True
