____ c.. _______ Counter


c_ Solution(o..
  ___ findAnagrams  s, p
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    sCount = Counter(s[:l..(p) - 1])
    pCount = Counter(p)
    ans    # list

    ___ i __ r..(l..(p) - 1, l..(s)):
      sCount[s[i]] += 1
      __ sCount __ pCount:
        ans.a..(i - l..(p) + 1)
      sCount[s[i - l..(p) + 1]] -= 1
      __ sCount[s[i - l..(p) + 1]] __ 0:
        del sCount[s[i - l..(p) + 1]]
    r.. ans
