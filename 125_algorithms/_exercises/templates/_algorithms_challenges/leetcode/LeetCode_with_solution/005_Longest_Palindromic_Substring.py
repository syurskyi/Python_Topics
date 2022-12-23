c_ Solution o..
    ___ longestPalindrome  s
        """
        :type s: str
        :rtype: str
        """
        # my solution
        # expand string according to Manacher algorithm
        # but extend radius step by step
        ls = l.. s)
        __ ls <= 1 or l.. s..(s)) __ 1:
            r_ s
        # create a new list like this: "abc"->"a#b#c"
        temp_s = '#'.join('{}'.f..(s))
        # print temp_s
        tls = l.. temp_s)
        seed = r.. 1, tls - 1)
        # this table stores the max length palindrome
        len_table = [0] * tls
        ___ step __ r.. 1, tls / 2 + 1
            final =    # list
            ___ pos __ seed:
                __ pos - step < 0 or pos + step >= tls:
                    c_
                __ temp_s[pos - step] != temp_s[pos + step]:
                    c_
                final.a.. pos)
                __ temp_s[pos - step] __ '#':
                    c_
                len_table[pos] = step
            seed = final
        max_pos, max_step = 0, 0
        ___ i, s __ e.. len_table
            __ s >= max_step:
                max_step = s
                max_pos = i
        r_ temp_s[max_pos - max_step:max_pos + max_step + 1].translate(N.., '#')

    # def longestPalindrome(self, s):
    #     # example in leetcode book
    #     max_left, max_right = 0, 0
    #     ls = len(s)
    #     for i in range(ls):
    #         len1 = self.expandAroundCenter(s, i, i)
    #         len2 = self.expandAroundCenter(s, i, i + 1)
    #         max_len = max(len1, len2)
    #         if (max_len > max_right - max_left):
    #             max_left = i - (max_len - 1) / 2
    #             max_right = i + max_len / 2
    #     return s[max_left:max_right + 1]
    #
    # def expandAroundCenter(self, s, left, right):
    #     ls = len(s)
    #     while (left >= 0 and right < ls and s[left] == s[right]):
    #         left -= 1
    #         right += 1
    #     return right - left - 1

    # def longestPalindrome(self, s):
    #     #Manacher algorithm
    #     #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    #     # Transform S into T.
    #     # For example, S = "abba", T = "^#a#b#b#a#$".
    #     # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    #     T = '#'.join('^{}$'.format(s))
    #     n = len(T)
    #     P = [0] * n
    #     C = R = 0
    #     for i in range (1, n-1):
    #         P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
    #         # Attempt to expand palindrome centered at i
    #         while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
    #             P[i] += 1
    #
    #         # If palindrome centered at i expand past R,
    #         # adjust center based on expanded palindrome.
    #         if i + P[i] > R:
    #             C, R = i, i + P[i]
    #
    #     # Find the maximum element in P.
    #     maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    #     return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]


__ ____ __ ____
    # begin
    s  ?
    print(s.longestPalindrome("abcbe"))
