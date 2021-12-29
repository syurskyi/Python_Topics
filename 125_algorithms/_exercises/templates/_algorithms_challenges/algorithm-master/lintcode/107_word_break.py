class Solution:
    """
    `dp[i]` means `s[:i]` is segmented by words
    """
    ___ wordBreak(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        __ n.. s and n.. words:
            r.. True
        __ n.. s o. n.. words:
            r.. False

        max_size = max(l..(w) ___ w __ words)
        word_set = set(words)

        n = l..(s)
        dp = [False] * (n + 1)
        dp[0] = True

        ___ i __ r..(1, n + 1):
            ___ j __ r..(1, m..(i, max_size) + 1):
                __ dp[i - j] and s[i - j:i] __ word_set:
                    dp[i] = True
                    break

        r.. dp[n]
