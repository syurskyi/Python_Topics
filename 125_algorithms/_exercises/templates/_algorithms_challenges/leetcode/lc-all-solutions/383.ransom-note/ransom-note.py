class Solution(object):
  ___ canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    letters = [0] * 26
    for c in magazine:
      letters[ord(c) - ord('a')] += 1

    for c in ransomNote:
      __ letters[ord(c) - ord('a')] == 0:
        return False
      else:
        letters[ord(c) - ord('a')] -= 1
    return True
