c_ Solution(o..
  ___ fullJustify  words, maxWidth
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    ans    # list
    line    # list
    lens = map(l.., words)
    idx = 0
    curLen = 0
    w.... idx < l..(words
      __ curLen __ 0:
        curLen = lens[idx]
      ____
        curLen += lens[idx] + 1
      line.a..(words[idx])
      idx += 1
      __ curLen > maxWidth:
        curLen = 0
        line.p.. )
        idx -= 1
        __ l..(line) __ 1:
          ans.a..(line[0] + " " * (maxWidth - l..(line[0])))
          line    # list
          _____
        spaces = maxWidth - s.. m..(l.., line
        avgSpace = spaces / (l..(line) - 1)
        extraSpace = spaces % (l..(line) - 1)
        res = ""
        ___ i __ r..(0, l..(line:
          res += line[i]
          __ i < l..(line) - 1:
            res += " " * (avgSpace + (extraSpace > 0
            extraSpace -= 1
        ans.a..(res)
        line    # list
      ____ idx __ l..(words
        res = ""
        ___ i __ r..(0, l..(line:
          res += line[i]
          __ i < l..(line) - 1:
            res += " "
        res += " " * (maxWidth - l..(res
        ans.a..(res)
    r.. ans
