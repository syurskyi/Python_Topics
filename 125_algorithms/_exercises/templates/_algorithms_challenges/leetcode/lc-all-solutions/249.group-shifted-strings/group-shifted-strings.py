class Solution(object):
  ___ groupStrings(self, strings):
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    ans = []
    single = []
    for s in strings:
      __ len(s) == 1:
        single.append(s)
        continue
      hashcodeArray = []
      pre = ord(s[0]) - ord("a")
      for i in range(1, len(s)):
        hashcodeArray.append(str(((ord(s[i]) - ord("a")) - pre) % 26))
        pre = ord(s[i]) - ord("a")
      hashcode = ",".join(hashcodeArray)
      __ hashcode not in d:
        d[hashcode] = [s]
      else:
        d[hashcode].append(s)
    for k in d:
      ans.append(d[k])
    __ single:
      ans.append(single)
    return ans
