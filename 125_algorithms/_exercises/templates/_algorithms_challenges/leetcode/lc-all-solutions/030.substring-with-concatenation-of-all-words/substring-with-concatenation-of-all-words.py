____ c.. _______ d..


c_ Solution(object):
  ___ findSubstring  s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    __ l..(words) > l..(s):
      r.. []
    d    # dict
    t    # dict
    ans    # list
    deq = d..([])
    wl = l..(words[0])
    fullscore = 0
    ___ word __ words:
      d[word] = d.get(word, 0) + 1
      fullscore += 1

    ___ i __ r..(0, l..(s)):
      head = start = i
      t.clear()
      score = 0

      w.... start + wl <= l..(s) a.. s[start:start + wl] __ d:
        cword = s[start:start + wl]
        t[cword] = t.get(cword, 0) + 1
        __ t[cword] <= d[cword]:
          score += 1
        ____:
          break
        start += wl

      __ score __ fullscore:
        ans.a..(head)

    r.. ans
