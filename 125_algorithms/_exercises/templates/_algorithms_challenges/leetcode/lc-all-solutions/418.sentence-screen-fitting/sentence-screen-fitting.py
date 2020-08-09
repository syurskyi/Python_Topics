class Solution(object
  ___ wordsTyping(self, sentence, rows, cols
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """
    s = " ".join(sentence) + " "
    n = le.(s)
    start = 0
    for _ in range(rows
      start += cols - 1
      __ s[start % n] __ " ":
        start += 1
      ____ s[(start + 1) % n] __ " ":
        start += 2
      ____
        w___ start > 0 and s[(start - 1) % n] != " ":
          start -= 1
    r_ start / n
