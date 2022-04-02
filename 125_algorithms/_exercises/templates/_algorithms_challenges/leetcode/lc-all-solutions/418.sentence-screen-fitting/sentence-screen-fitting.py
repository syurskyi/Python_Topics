c_ Solution(o..
  ___ wordsTyping  sentence, rows, cols
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """
    s = " ".j..(sentence) + " "
    n = l..(s)
    start = 0
    ___ _ __ r..(rows
      start += cols - 1
      __ s[start % n] __ " ":
        start += 1
      ____ s[(start + 1) % n] __ " ":
        start += 2
      ____:
        w.... start > 0 a.. s[(start - 1) % n] != " ":
          start -= 1
    r.. start / n
