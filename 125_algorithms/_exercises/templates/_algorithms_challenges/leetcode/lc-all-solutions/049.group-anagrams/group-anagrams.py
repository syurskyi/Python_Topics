class Solution(object
  ___ groupAnagrams(self, strs
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    ___ hash(count
      p1, p2 = 2903, 29947
      ret = 0
      ___ c in count:
        ret = ret * p1 + c
        p1 *= p2
      r_ ret

    d = {}

    ___ str in strs:
      count = [0] * 26
      ___ c in str:
        count[ord(c) - ord('a')] += 1
      key = hash(count)
      __ key not in d:
        d[key] = [str]
      ____
        d[key].append(str)
    r_ [d[k] ___ k in d]
