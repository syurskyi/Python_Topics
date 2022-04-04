c_ Solution(o..
  ___ findAllConcatenatedWordsInADict  words
    """
    :type words: List[str]
    :rtype: List[str]
    """

    ___ wordBreak(word, cands
      __ n.. cands:
        r.. F..
      dp = [F..] * (l..(word) + 1)
      dp[0] = T..
      ___ i __ r..(1, l..(word) + 1
        ___ j __ r..(r..(0, i:
          __ n.. dp[j]:
            _____
          __ word[j:i] __ cands:
            dp[i] = T..
            _____
      r.. dp[-1]

    words.s..(key=l.... x: -l..(x
    cands = s..(words)
    ans    # list
    ___ i __ r..(0, l..(words:
      cands -= {words[i]}
      __ wordBreak(words[i], cands
        ans += words[i],
    r.. ans
