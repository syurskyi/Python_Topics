c_ Solution(o..):
  ___ validIPAddress  IP):
    """
    :type IP: str
    :rtype: str
    """
    nums = [s..(i) ___ i __ r..(0, 10)]
    letters = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]
    v6d = set(nums + letters)
    v4d = set(nums)

    v4 = IP.s..(".")
    v6 = IP.s..(":")

    __ l..(v4) __ 4:
      ___ seg __ v4:
        __ seg __ "" o. (seg[0] __ "0" a.. l..(seg) > 1):
          r.. "Neither"
        ___ c __ seg:
          __ c n.. __ v4d:
            r.. "Neither"
        __ i..(seg) > 255:
          r.. "Neither"
      r.. "IPv4"
    ____ l..(v6) __ 8:
      ___ seg __ v6:
        __ l..(seg) __ 0 o. l..(seg) > 4:
          r.. "Neither"
        ___ c __ seg:
          __ c n.. __ v6d:
            r.. "Neither"
      r.. "IPv6"
    r.. "Neither"
