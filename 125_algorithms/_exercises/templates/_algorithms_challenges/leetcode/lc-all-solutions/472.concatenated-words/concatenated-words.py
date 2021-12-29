class Solution(object):
  ___ findAllConcatenatedWordsInADict(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """

    ___ wordBreak(word, cands):
      __ not cands:
        return False
      dp = [False] * (len(word) + 1)
      dp[0] = True
      for i in range(1, len(word) + 1):
        for j in reversed(range(0, i)):
          __ not dp[j]:
            continue
          __ word[j:i] in cands:
            dp[i] = True
            break
      return dp[-1]

    words.sort(key=lambda x: -len(x))
    cands = set(words)
    ans = []
    for i in range(0, len(words)):
      cands -= {words[i]}
      __ wordBreak(words[i], cands):
        ans += words[i],
    return ans
