______ collections


class Solution(object
  ___ findLongestWord(self, s, d
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    d.sort(key=lambda x: (-le.(x), x))

    ___ isSubseq(word, s
      i = 0
      for c in s:
        __ c __ word[i]:
          i += 1
        __ i __ le.(word
          r_ True
      r_ False

    for word in d:
      __ isSubseq(word, s
        r_ word
    r_ ""
