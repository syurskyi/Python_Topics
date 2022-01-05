c_ Solution(o..):
  ___ readBinaryWatch  num):
    """
    :type num: int
    :rtype: List[str]
    """
    ans    # list
    ___ i __ r..(0, 12):
      ___ j __ r..(0, 60):
        __ (bin(i) + bin(j)).c.. "1") __ num:
          ans.a..("%d:%02d" % (i, j))
    r.. ans
