from collections import deque


class Solution(object):
  ___ findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    __ len(words) > len(s):
      return []
    d = {}
    t = {}
    ans = []
    deq = deque([])
    wl = len(words[0])
    fullscore = 0
    for word in words:
      d[word] = d.get(word, 0) + 1
      fullscore += 1

    for i in range(0, len(s)):
      head = start = i
      t.clear()
      score = 0

      while start + wl <= len(s) and s[start:start + wl] in d:
        cword = s[start:start + wl]
        t[cword] = t.get(cword, 0) + 1
        __ t[cword] <= d[cword]:
          score += 1
        else:
          break
        start += wl

      __ score == fullscore:
        ans.append(head)

    return ans
