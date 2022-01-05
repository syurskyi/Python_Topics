c_ Solution(object):
  ___ generatePossibleNextMoves  s):
    """
    :type s: str
    :rtype: List[str]
    """
    ans    # list
    ___ i __ r..(0, l..(s) - 1):
      __ s[i:i + 2] __ "++":
        ans.a..(s[:i] + "--" + s[i + 2:])
    r.. ans
