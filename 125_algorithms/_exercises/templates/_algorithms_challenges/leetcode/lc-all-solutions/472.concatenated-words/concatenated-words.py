class Solution(object
  ___ findAllConcatenatedWordsInADict(self, words
    """
    :type words: List[str]
    :rtype: List[str]
    """

    ___ wordBreak(word, cands
      __ not cands:
        r_ False
      dp = [False] * (le.(word) + 1)
      dp[0] = True
      ___ i __ range(1, le.(word) + 1
        ___ j __ reversed(range(0, i)):
          __ not dp[j]:
            continue
          __ word[j:i] __ cands:
            dp[i] = True
            break
      r_ dp[-1]

    words.sort(key=lambda x: -le.(x))
    cands = set(words)
    ans =   # list
    ___ i __ range(0, le.(words)):
      cands -= {words[i]}
      __ wordBreak(words[i], cands
        ans += words[i],
    r_ ans
