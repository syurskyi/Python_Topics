____ c.. _______ C..


c_ Solution(o..
  ___ findAnagrams  s, p
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    sCount = C..(s[:l..(p) - 1])
    pCount = C..(p)
    ans    # list

    ___ i __ r..(l..(p) - 1, l..(s:
      sCount[s[i]] += 1
      __ sCount __ pCount:
        ans.a..(i - l..(p) + 1)
      sCount[s[i - l..(p) + 1]] -= 1
      __ sCount[s[i - l..(p) + 1]] __ 0:
        del sCount[s[i - l..(p) + 1]]
    r.. ans
