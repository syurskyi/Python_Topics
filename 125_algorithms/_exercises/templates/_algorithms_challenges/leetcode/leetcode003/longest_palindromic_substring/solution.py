c_ Solution:
    # @return a string
    ___ longestPalindrome(self, s):
        n = l..(s)
        t = [[F.. ___ i __ r..(n)] ___ j __ r..(n)]
        start = 0
        max_len = 1
        ___ i __ r..(n):
            t[i][i] = T..
        ___ i __ r..(n - 1):
            j = i + 1
            __ s[i] __ s[j]:
                t[i][j] = T..
                start = i
                max_len = 2
        ___ l __ r..(3, n + 1):
            ___ i __ r..(n - l + 1):
                j = i + l - 1
                __ s[i] __ s[j] a.. t[i + 1][j - 1]:
                    t[i][j] = T..
                    start = i
                    max_len = l
        r.. s[start:start + max_len]


a = 'akaa2baakcbbc'
s = Solution()
print s.longestPalindrome(a)
