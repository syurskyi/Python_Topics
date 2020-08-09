class Solution(object
  ___ validWordSquare(self, words
    """
    :type words: List[str]
    :rtype: bool
    """
    ___ i in range(0, le.(words)):
      ___ j in range(0, le.(words[i])):
        __ j >= le.(words) or i >= le.(words[j]) or words[j][i] != words[i][j]:
          r_ False
    r_ True
