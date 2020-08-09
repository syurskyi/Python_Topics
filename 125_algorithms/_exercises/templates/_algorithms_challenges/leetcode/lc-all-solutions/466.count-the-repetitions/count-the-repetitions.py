class Solution(object
  ___ getMaxRepetitions(self, s1, n1, s2, n2
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    l2 = le.(s2)
    dp = [0] * l2
    ___ i in range(l2
      j = i
      ___ c in s1:
        __ c __ s2[j % l2]:
          j += 1
      __ j __ i:
        r_ 0
      dp[i] = j - i

    idx = 0
    ___ i in range(n1
      idx += dp[idx % l2]
    r_ idx / l2 / n2
