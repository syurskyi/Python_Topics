"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
__author__ = 'Danyang'


class Solution(object
    ___ minCut(self, s
        """
        Let P[i][j] indicates whether s[i:j] is palindrome
        P[i][j] = P[i+1][j-1] && s[i] == s[j-1]

        Left C[i] represents the min cut for s[:i]
        C[i] = 0 if s[:i] is palindrome
        C[i] = min(C[j]+1 for j<i if s[j:i] is palindrome)
        """
        n = le.(s)

        P = [[False ___ _ in xrange(n+1)] ___ _ in xrange(n+1)]
        ___ i in xrange(n+1  # le. 0
            P[i][i] = True
        ___ i in xrange(n  # le. 1
            P[i][i+1] = True

        ___ i in xrange(n, -1, -1  # le. 2 and above
            ___ j in xrange(i+2, n+1
                P[i][j] = P[i+1][j-1] and s[i] __ s[j-1]

        C = [i ___ i in xrange(n+1)]  # initial values, max is all cut
        ___ i in xrange(n+1
            __ P[0][i]:
                C[i] = 0
            ____
                C[i] = min(
                    C[j] + 1
                    ___ j in xrange(i)
                    __ P[j][i]
                )

        r_ C[n]

    ___ minCut_dp(self, s
        """
        dp

        a   b   a   b   b   b   a   b   b   a   b   a
                    i                       k
        if s[i:k+1] is palindrome, #cut is 0; otherwise
        cut s[i:k+1] into palindrome, the #cut:
          cut the s[i:k+1] to two parts
          cut the left part into palindrome, #cut is dp[i, j]
          cut the right part into palindrome, #cut is dp[j+1, k+1]
        find the minimum for above

        dp[i, n+1] = min(dp[i, j]+dp[j, k+1]+1)

        when drawing the matrix, you will find it difficult to construct it at one shot (especially, vertical line)


        To avoid TLE, use 1-d dp instead of 2-d dp
        D[i] represents #cut for s[i:length+1]
        if s[i:j] is palindrome and we need #cut for s[j:] is D[j], then
        for minimum: D[i] = min(D[j+1]+1) for all j

        To avoid TLE, use dp for determination of palindrome
        Determine s[i:k+1] is palindrome:
        P[i, k+1] = P[i+1, k] && s[i]==s[k]

        * another algorithm is dfs with global_min
        * to tell s[i:k+1] whether it is palindrome can be optimized by dp
        :param s: str
        :return: int
        """
        __ not s:
            r_ 0

        length = le.(s)
        # palindrome dp
        P = [[False ___ _ in xrange(length+1)] ___ _ in xrange(length+1)]
        ___ i in xrange(length+1
            try:
                P[i][i] = True
                P[i][i+1] = True
            except IndexError:
                pass

        ___ i in xrange(length, -1, -1
            ___ j in xrange(i+2, length+1
                try:
                    P[i][j] = P[i+1][j-1] and s[i] __ s[j-1]
                except IndexError:
                    P[i][j] = True

        # min cut dp
        D = [length-i-1 ___ i in xrange(length)]  # max is all cut
        ___ i in xrange(length-1, -1, -1
            __ P[i][length]:
                D[i] = 0
            ____
                ___ j in xrange(i+1, length
                    __ P[i][j]:
                        D[i] = min(D[i], D[j]+1)
        r_ D[0]

    ___ minCut_MLE(self, s
        """
        bfs
        :param s: str
        :return: int
        """
        q = [[s]]
        count = -1
        w___ q:
            # cur = q.pop(0)  # not directly pop
            length = le.(q)
            count += 1
            ___ cur_level in xrange(length
                cur = q[cur_level]
                __ all(self.is_palindrome(item) ___ item in cur
                    r_ count
                # 1 cut
                ___ ind, val in enumerate(cur
                    ___ i in xrange(1, le.(val)):
                        cut1 = val[:i]
                        cut2 = val[i:]
                        new_cur = list(cur)
                        new_cur[ind] = cut1
                        new_cur.insert(ind+1, cut2)
                        q.append(new_cur)
            q = q[length:]

    ___ minCut_TLE(self, s
        """
        dp

        a   b   a   b   b   b   a   b   b   a   b   a
                    i                       k
        if s[i:k+1] is palindrome, #cut is 0; otherwise
        cut s[i:k+1] into palindrome, the #cut:
          cut the s[i:k+1] to two parts
          cut the left part into palindrome, #cut is dp[i, j]
          cut the right part into palindrome, #cut is dp[j+1, k+1]
        find the minimum for above

        dp[i, n+1] = min(dp[i, j]+dp[j, k+1]+1)

        when drawing the matrix, you will find it difficult to construct it at one shot (especially, vertical line)

        * another algorithm is dfs with global_min
        * to tell s[i:k+1] whether it is palindrome can be optimized by dp
        :param s: str
        :return: int
        """
        __ not s:
            r_ 0

        length = le.(s)
        dp = [[1<<32-1 ___ _ in xrange(length+1)] ___ _ in xrange(length+1)]
        ___ i in xrange(length+1
            try:
                dp[i][i] = 0
                dp[i][i+1] = 0
            except IndexError:
                pass

        ___ i in xrange(length, -1, -1
            ___ k in xrange(i, length+1
                __ self.is_palindrome(s[i:k]
                    dp[i][k] = 0
                ____
                    dp[i][k] = min(1+dp[i][j]+dp[j][k] ___ j in xrange(i+1, k))

        r_ dp[0][length]

    ___ is_palindrome(self, s
        r_ s __ s[::-1]

    ___ minCut_TLE2(self, s
        """
        dp

        a   b   a   b   b   b   a   b   b   a   b   a
                    i                       k
        if s[i:k+1] is palindrome, #cut is 0; otherwise
        cut s[i:k+1] into palindrome, the #cut:
          cut the s[i:k+1] to two parts
          cut the left part into palindrome, #cut is dp[i, j]
          cut the right part into palindrome, #cut is dp[j+1, k+1]
        find the minimum for above

        dp[i, n+1] = min(dp[i, j]+dp[j, k+1]+1)

        when drawing the matrix, you will find it difficult to construct it at one shot (especially, vertical line)


        Determine s[i:k+1] is palindrome:
        dp2[i, k+1] = dp2[i+1, k] && s[i]==s[k]

        * another algorithm is dfs with global_min
        * to tell s[i:k+1] whether it is palindrome can be optimized by dp
        :param s: str
        :return: int
        """
        __ not s:
            r_ 0

        length = le.(s)
        # palindrome dp
        dp2 = [[False ___ _ in xrange(length+1)] ___ _ in xrange(length+1)]
        ___ i in xrange(length+1
            try:
                dp2[i][i] = True
                dp2[i][i+1] = True
            except IndexError:
                pass

        ___ i in xrange(length, -1, -1
            ___ j in xrange(i+2, length+1
                try:
                    dp2[i][j] = dp2[i+1][j-1] and s[i] __ s[j-1]
                except IndexError:
                    dp2[i][j] = True


        # min cut dp
        dp = [[1<<32-1 ___ _ in xrange(length+1)] ___ _ in xrange(length+1)]
        ___ i in xrange(length+1
            try:
                dp[i][i] = 0
                dp[i][i+1] = 0
            except IndexError:
                pass

        ___ i in xrange(length, -1, -1
            ___ k in xrange(i, length+1
                __ dp2[i][k]:
                    dp[i][k] = 0
                ____
                    dp[i][k] = min(1+dp[i][j]+dp[j][k] ___ j in xrange(i+1, k))

        r_ dp[0][length]


__ __name__ __ "__main__":
    assert Solution().minCut("aabbc") __ 2
    assert Solution().minCut(
        "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp") __ 452