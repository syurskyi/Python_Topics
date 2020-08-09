class Solution(object
  ___ groupStrings(self, strings
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    ans = []
    single = []
    ___ s in strings:
      __ le.(s) __ 1:
        single.append(s)
        continue
      hashcodeArray = []
      pre = ord(s[0]) - ord("a")
      ___ i in range(1, le.(s)):
        hashcodeArray.append(str(((ord(s[i]) - ord("a")) - pre) % 26))
        pre = ord(s[i]) - ord("a")
      hashcode = ",".join(hashcodeArray)
      __ hashcode not in d:
        d[hashcode] = [s]
      ____
        d[hashcode].append(s)
    ___ k in d:
      ans.append(d[k])
    __ single:
      ans.append(single)
    r_ ans
