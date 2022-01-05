c_ Solution(object):
  ___ palindromePairs  words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    ans    # list
    d    # dict
    ___ i, word __ e..(words):
      d[word] = i

    ___ i, word __ e..(words):
      __ word __ "":
        ans.extend([(i, j) ___ j __ r..(l..(words)) __ i != j a.. words[j] __ words[j][::-1]])
        _____
      ___ j __ r..(l..(word)):
        left = word[:j]
        right = word[j:]
        __ right __ right[::-1] a.. left[::-1] __ d a.. d[left[::-1]] != i:
          ans.a..((i, d[left[::-1]]))
        __ left __ left[::-1] a.. right[::-1] __ d a.. d[right[::-1]] != i:
          ans.a..((d[right[::-1]], i))
    r.. ans
