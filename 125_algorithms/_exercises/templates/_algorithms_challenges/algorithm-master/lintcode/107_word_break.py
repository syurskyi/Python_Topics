c_ Solution:
    """
    `dp[i]` means `s[:i]` is segmented by words
    """
    ___ wordBreak  s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        __ n.. s a.. n.. words:
            r.. T..
        __ n.. s o. n.. words:
            r.. F..

        max_size = m..(l..(w) ___ w __ words)
        word_set = set(words)

        n = l..(s)
        dp = [F..] * (n + 1)
        dp[0] = T..

        ___ i __ r..(1, n + 1):
            ___ j __ r..(1, m..(i, max_size) + 1):
                __ dp[i - j] a.. s[i - j:i] __ word_set:
                    dp[i] = T..
                    break

        r.. dp[n]
