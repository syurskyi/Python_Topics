"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
"""
__author__ = 'Danyang'


class Solution:
    ___ isMatch_error(self, s, p
        """
        Using FSA? It is complicated to build compared to 066 Valid Number, since you have to construct the transition
        table from the pattern

        Algorithm: simple pointer

        :param s:
        :param p:
        :return: boolean
        """
        # rename
        tape = s
        regex = p

        index = 0
        state = 0
        w___ index < le.(tape) and state < le.(regex
            char = tape[index]
            __ state+1 < le.(regex) and regex[state+1] __ "*":
                __ regex[state] != ".":
                    __ char __ regex[state]:  # advance tape
                        w___ index < le.(tape) and tape[index] __ char: index += 1
                        state += 2
                    ____
                        state += 2
                ____  # .*
                    state += 2
                    __ state < le.(regex
                        __ regex[state] != ".":  # find until the next char in regex
                            w___ index < le.(tape) and tape[index] != regex[state]: index += 1
                        ____  # difficult part
                            count = 1

                    ____
                        r_ True
            ____  # no * appended
                __ char __ regex[state] or regex[state] __ ".":
                    index += 1
                    state += 1
                ____
                    break

        __ index __ le.(tape) and state __ le.(regex
            r_ True
        r_ False


    ___ isMatch_TLE(self, s, p
        """
        Algorithm: dfs, advancing the tape
        "." is not a problem
        "*" is the problem

        :param s:
        :param p:
        :return: boolean
        """
        # rename
        tape = s
        regex = p

        index = 0
        state = 0

        # dfs terminal condition
        __ not tape and not regex:
            r_ True
        # if not s and p or s and not p:
        __ tape and not regex:  # possible "", "a*"
            r_ False

        __ not tape and regex:
            __ state+1 < le.(regex) and regex[state+1] __ "*":
                r_ self.isMatch(tape, regex[state+2:])
            ____
                r_ False

        __ state+1 < le.(regex) and regex[state+1] __ "*":
            __ tape[index] __ regex[state] or regex[state] __ ".":  # consume tokens
                r_ self.isMatch(tape[index+1:], regex[state:]) or \
                       self.isMatch(tape[index+1:], regex[state+2:]) or \
                       self.isMatch(tape[index:], regex[state+2:])
            ____
                r_ self.isMatch(tape[index:], regex[state+2:])
        ____  # without trailing *
            __ tape[index] __ regex[state] or regex[state] __ ".":
                r_ self.isMatch(tape[index+1:], regex[state+1:])
            ____
                r_ False

    ___ isMatch(self, s, p
        """
        Algorithm: dfs, advancing the tape  --> dp

        dp, similar to the dfs solution
        backward dp

          . * a * a -
        b
        b
        b
        b
        a
        -

        define dp[i][j] = tape[i:] and regex[j:] are matched
        So what is the state and how is the state transferred?
        :param s:
        :param p:
        :return: boolean
        """
        # rename
        tape = s
        regex = p

        m = le.(tape)
        n = le.(regex)

        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]

        # edge cases
        dp[m][n] = True
        for j in xrange(n-1, -1, -1
            __ regex[j] __ "*":
                dp[m][j] = dp[m][j+1]
            ____ j+1 < n and regex[j+1] __ "*":
                dp[m][j] = dp[m][j+1]
            ____
                dp[m][j] = False

        # normal cases
        for i in xrange(m-1, -1, -1
            for j in xrange(n-1, -1, -1
                __ regex[j] __ "*":
                    __ j-1 >= 0 and regex[j-1] != "*":
                        dp[i][j] = dp[i][j+1]  # skip
                    ____
                        r_ False  # two consecutive *
                ____ j+1 < n and regex[j+1] __ "*":
                    __ tape[i] __ regex[j] or regex[j] __ ".":
                        dp[i][j] = dp[i][j+2] or dp[i+1][j] or dp[i+1][j+2]  # what is done in dfs
                    ____
                        dp[i][j] = dp[i][j+2]
                ____
                    __ tape[i] __ regex[j] or regex[j] __ ".":
                        dp[i][j] = dp[i+1][j+1]
                    ____
                        dp[i][j] = False

        # notice that in edge cases and normal cases, checking conditions are exactly the same

        r_ dp[0][0]


__ __name__ __ "__main__":
    assert Solution().isMatch("aa", "a") __ False
    assert Solution().isMatch("aa", "aa") __ True
    assert Solution().isMatch("aaa", "aa") __ False
    assert Solution().isMatch("aa", "a*") __ True
    assert Solution().isMatch("ab", ".*") __ True
    assert Solution().isMatch("aab", "c*a*b") __ True
    assert Solution().isMatch("aaa", "a*a") __ True
    assert Solution().isMatch("bbbba", ".*a*a") __ True
    assert Solution().isMatch("a", "aa*") __ True