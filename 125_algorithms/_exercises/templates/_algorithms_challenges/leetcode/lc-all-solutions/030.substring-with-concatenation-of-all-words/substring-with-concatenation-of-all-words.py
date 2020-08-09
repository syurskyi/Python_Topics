from collections ______ deque


class Solution(object
  ___ findSubstring(self, s, words
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    __ le.(words) > le.(s
      r_ []
    d = {}
    t = {}
    ans = []
    deq = deque([])
    wl = le.(words[0])
    fullscore = 0
    for word in words:
      d[word] = d.get(word, 0) + 1
      fullscore += 1

    for i in range(0, le.(s)):
      head = start = i
      t.clear()
      score = 0

      w___ start + wl <= le.(s) and s[start:start + wl] in d:
        cword = s[start:start + wl]
        t[cword] = t.get(cword, 0) + 1
        __ t[cword] <= d[cword]:
          score += 1
        ____
          break
        start += wl

      __ score __ fullscore:
        ans.append(head)

    r_ ans
