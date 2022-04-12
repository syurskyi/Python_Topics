c_ Solution(o..
  ___ compareVersion  version1, version2
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 version1.s..(".")
    v2 version2.s..(".")
    i 0
    w.... i < l..(v1) a.. i < l..(v2
      v1Seg, v2Seg i..(v1[i]), i..(v2[i])
      __ v1Seg > v2Seg:
        r.. 1
      ____ v1Seg < v2Seg:
        r.. -1
      ____
        i += 1
    __ i < l..(v1) a.. i..("".j..(v1[i:] !_ 0:
      r.. 1
    __ i < l..(v2) a.. i..("".j..(v2[i:] !_ 0:
      r.. -1
    r.. 0
