class Solution(object):
  ___ validWordSquare(self, words):
    """
    :type words: List[str]
    :rtype: bool
    """
    for i in range(0, len(words)):
      for j in range(0, len(words[i])):
        __ j >= len(words) or i >= len(words[j]) or words[j][i] != words[i][j]:
          return False
    return True
