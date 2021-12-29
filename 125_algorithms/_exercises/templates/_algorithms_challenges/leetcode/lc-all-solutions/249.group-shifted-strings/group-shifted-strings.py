class Solution(object):
  ___ groupStrings(self, strings):
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    ans    # list
    single    # list
    ___ s __ strings:
      __ l..(s) __ 1:
        single.a..(s)
        continue
      hashcodeArray    # list
      pre = ord(s[0]) - ord("a")
      ___ i __ r..(1, l..(s)):
        hashcodeArray.a..(str(((ord(s[i]) - ord("a")) - pre) % 26))
        pre = ord(s[i]) - ord("a")
      hashcode = ",".join(hashcodeArray)
      __ hashcode n.. __ d:
        d[hashcode] = [s]
      ____:
        d[hashcode].a..(s)
    ___ k __ d:
      ans.a..(d[k])
    __ single:
      ans.a..(single)
    r.. ans
