c_ Solution(object):
  ___ groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    ___ hash(count):
      p1, p2 = 2903, 29947
      ret = 0
      ___ c __ count:
        ret = ret * p1 + c
        p1 *= p2
      r.. ret

    d    # dict

    ___ s.. __ strs:
      count = [0] * 26
      ___ c __ s..:
        count[ord(c) - ord('a')] += 1
      key = hash(count)
      __ key n.. __ d:
        d[key] = [s..]
      ____:
        d[key].a..(s..)
    r.. [d[k] ___ k __ d]
