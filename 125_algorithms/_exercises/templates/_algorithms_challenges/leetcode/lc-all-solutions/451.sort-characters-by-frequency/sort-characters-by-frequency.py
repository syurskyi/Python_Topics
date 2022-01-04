____ c.. _______ Counter


c_ Solution(object):
  ___ frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    d = Counter(s)
    buf    # dict
    ___ k, v __ d.i..:
      buf[v] = buf.get(v, "") + k * v
    ans = ""
    ___ i __ r..(r..(0, l..(s))):
      ans += buf.get(i, "")
    r.. ans
