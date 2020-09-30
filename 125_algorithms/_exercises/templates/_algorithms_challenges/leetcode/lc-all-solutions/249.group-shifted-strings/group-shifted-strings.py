class Solution(object
  ___ groupStrings(self, strings
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    ans =   # list
    single =   # list
    ___ s __ strings:
      __ le.(s) __ 1:
        single.append(s)
        continue
      hashcodeArray =   # list
      pre = ord(s[0]) - ord("a")
      ___ i __ range(1, le.(s)):
        hashcodeArray.append(str(((ord(s[i]) - ord("a")) - pre) % 26))
        pre = ord(s[i]) - ord("a")
      hashcode = ",".join(hashcodeArray)
      __ hashcode not __ d:
        d[hashcode] = [s]
      ____
        d[hashcode].append(s)
    ___ k __ d:
      ans.append(d[k])
    __ single:
      ans.append(single)
    r_ ans
