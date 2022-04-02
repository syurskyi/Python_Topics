c_ Solution(o..
  ___ validWordSquare  words
    """
    :type words: List[str]
    :rtype: bool
    """
    ___ i __ r..(0, l..(words)):
      ___ j __ r..(0, l..(words[i])):
        __ j >= l..(words) o. i >= l..(words[j]) o. words[j][i] != words[i][j]:
          r.. F..
    r.. T..
