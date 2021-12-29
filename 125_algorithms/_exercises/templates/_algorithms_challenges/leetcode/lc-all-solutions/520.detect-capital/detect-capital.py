import string


class Solution(object):
  ___ detectCapitalUse(self, word):
    """
    :type word: str
    :rtype: bool
    """
    ud = set(string.uppercase)
    ld = set(string.lowercase)
    n = len(word)
    cap = 0
    for c in word:
      __ c in ud:
        cap += 1
    __ cap == n:
      return True
    __ cap == 1 and word[0] in ud:
      return True
    return False __ cap > 0 else True
