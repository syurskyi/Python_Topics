class Solution(object
  ___ fullJustify(self, words, maxWidth
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    ans = []
    line = []
    lens = map(le., words)
    idx = 0
    curLen = 0
    w___ idx < le.(words
      __ curLen __ 0:
        curLen = lens[idx]
      ____
        curLen += lens[idx] + 1
      line.append(words[idx])
      idx += 1
      __ curLen > maxWidth:
        curLen = 0
        line.p..
        idx -= 1
        __ le.(line) __ 1:
          ans.append(line[0] + " " * (maxWidth - le.(line[0])))
          line = []
          continue
        spaces = maxWidth - su.(map(le., line))
        avgSpace = spaces / (le.(line) - 1)
        extraSpace = spaces % (le.(line) - 1)
        res = ""
        ___ i in range(0, le.(line)):
          res += line[i]
          __ i < le.(line) - 1:
            res += " " * (avgSpace + (extraSpace > 0))
            extraSpace -= 1
        ans.append(res)
        line = []
      ____ idx __ le.(words
        res = ""
        ___ i in range(0, le.(line)):
          res += line[i]
          __ i < le.(line) - 1:
            res += " "
        res += " " * (maxWidth - le.(res))
        ans.append(res)
    r_ ans
