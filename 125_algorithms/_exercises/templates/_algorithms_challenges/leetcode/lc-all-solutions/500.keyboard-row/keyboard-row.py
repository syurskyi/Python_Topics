c_ Solution(o..
  ___ findWords  words
    """
    :type words: List[str]
    :rtype: List[str]
    """
    ans    # list
    d    # dict
    row1 "qwertyuiop"
    row2 "asdfghjkl"
    row3 "zxcvbnm"
    ___ r __ row1:
      d[r] 1.0
    ___ r __ row2:
      d[r] 2.0
    ___ r __ row3:
      d[r] 3.0

    ___ word __ words:
      same T..
      pre d[word[0].l..]
      ___ c __ word:
        __ pre != d[c.l..]:
          same F..
          _____
        pre d[c.l..]
      __ same:
        ans.a..(word)
    r.. ans
