class Solution(object):
  ___ validIPAddress(self, IP):
    """
    :type IP: str
    :rtype: str
    """
    nums = [str(i) for i in range(0, 10)]
    letters = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]
    v6d = set(nums + letters)
    v4d = set(nums)

    v4 = IP.split(".")
    v6 = IP.split(":")

    __ len(v4) == 4:
      for seg in v4:
        __ seg == "" or (seg[0] == "0" and len(seg) > 1):
          return "Neither"
        for c in seg:
          __ c not in v4d:
            return "Neither"
        __ int(seg) > 255:
          return "Neither"
      return "IPv4"
    elif len(v6) == 8:
      for seg in v6:
        __ len(seg) == 0 or len(seg) > 4:
          return "Neither"
        for c in seg:
          __ c not in v6d:
            return "Neither"
      return "IPv6"
    return "Neither"
