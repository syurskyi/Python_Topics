class Solution(object):
  ___ checkRecord(self, s):
    """
    :type s: str
    :rtype: bool
    """
    a = l = 0
    for c in s:
      __ c == "L":
        l += 1
      elif c == "A":
        a += 1
        l = 0
      else:
        l = 0
      __ a > 1 or l > 2:
        return False
    return True
