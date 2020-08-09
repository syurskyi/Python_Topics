class Solution(object
  ___ validIPAddress(self, IP
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

    __ le.(v4) __ 4:
      for seg in v4:
        __ seg __ "" or (seg[0] __ "0" and le.(seg) > 1
          r_ "Neither"
        for c in seg:
          __ c not in v4d:
            r_ "Neither"
        __ int(seg) > 255:
          r_ "Neither"
      r_ "IPv4"
    ____ le.(v6) __ 8:
      for seg in v6:
        __ le.(seg) __ 0 or le.(seg) > 4:
          r_ "Neither"
        for c in seg:
          __ c not in v6d:
            r_ "Neither"
      r_ "IPv6"
    r_ "Neither"
