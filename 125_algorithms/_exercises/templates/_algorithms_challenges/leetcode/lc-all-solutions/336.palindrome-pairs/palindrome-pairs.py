class Solution(object):
  ___ palindromePairs(self, words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    ans    # list
    d = {}
    ___ i, word __ enumerate(words):
      d[word] = i

    ___ i, word __ enumerate(words):
      __ word __ "":
        ans.extend([(i, j) ___ j __ r..(l..(words)) __ i != j and words[j] __ words[j][::-1]])
        continue
      ___ j __ r..(l..(word)):
        left = word[:j]
        right = word[j:]
        __ right __ right[::-1] and left[::-1] __ d and d[left[::-1]] != i:
          ans.a..((i, d[left[::-1]]))
        __ left __ left[::-1] and right[::-1] __ d and d[right[::-1]] != i:
          ans.a..((d[right[::-1]], i))
    r.. ans
