c_ Solution(o..
  ___ maxProduct  words
    """
    :type words: List[str]
    :rtype: int
    """
    bitmap [0] * l..(words)
    mask 0x01
    ans 0
    ___ i __ r..(0, l.. ?
      word words[i]
      ___ c __ word:
        bitmap[i] |= (mask << (o..(c) - o..('a')))
    ___ i __ r..(0, l.. ?
      ___ j __ r..(0, i
        __ bitmap[i] & bitmap[j] __ 0:
          ans m..(ans, l..(words[i]) * l..(words[j]

    r.. ans
