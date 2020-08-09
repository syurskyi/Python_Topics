class Solution(object
  ___ findWords(self, words
    """
    :type words: List[str]
    :rtype: List[str]
    """
    ans = []
    d = {}
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    ___ r in row1:
      d[r] = 1.0
    ___ r in row2:
      d[r] = 2.0
    ___ r in row3:
      d[r] = 3.0

    ___ word in words:
      same = True
      pre = d[word[0].lower()]
      ___ c in word:
        __ pre != d[c.lower()]:
          same = False
          break
        pre = d[c.lower()]
      __ same:
        ans.append(word)
    r_ ans
