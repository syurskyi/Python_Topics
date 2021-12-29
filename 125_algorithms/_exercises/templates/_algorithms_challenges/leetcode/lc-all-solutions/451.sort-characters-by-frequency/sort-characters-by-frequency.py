____ collections _______ Counter


class Solution(object):
  ___ frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    d = Counter(s)
    buf = {}
    ___ k, v __ d.items():
      buf[v] = buf.get(v, "") + k * v
    ans = ""
    ___ i __ reversed(r..(0, l..(s))):
      ans += buf.get(i, "")
    r.. ans
