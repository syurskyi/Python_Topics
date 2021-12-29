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
    ___ isMatch_error(self, s, p):
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
        w.... index < l..(tape) a.. state < l..(regex):
            char = tape[index]
            __ state+1 < l..(regex) a.. regex[state+1] __ "*":
                __ regex[state] != ".":
                    __ char __ regex[state]:  # advance tape
                        w.... index < l..(tape) a.. tape[index] __ char: index += 1
                        state += 2
                    ____:
                        state += 2
                ____:  # .*
                    state += 2
                    __ state < l..(regex):
                        __ regex[state] != ".":  # find until the next char in regex
                            w.... index < l..(tape) a.. tape[index] != regex[state]: index += 1
                        ____:  # difficult part
                            count = 1

                    ____:
                        r.. True
            ____:  # no * appended
                __ char __ regex[state] o. regex[state] __ ".":
                    index += 1
                    state += 1
                ____:
                    break

        __ index __ l..(tape) a.. state __ l..(regex):
            r.. True
        r.. False


    ___ isMatch_TLE(self, s, p):
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
        __ n.. tape a.. n.. regex:
            r.. True
        # if not s and p or s and not p:
        __ tape a.. n.. regex:  # possible "", "a*"
            r.. False

        __ n.. tape a.. regex:
            __ state+1 < l..(regex) a.. regex[state+1] __ "*":
                r.. self.isMatch(tape, regex[state+2:])
            ____:
                r.. False

        __ state+1 < l..(regex) a.. regex[state+1] __ "*":
            __ tape[index] __ regex[state] o. regex[state] __ ".":  # consume tokens
                r.. self.isMatch(tape[index+1:], regex[state:]) o. \
                       self.isMatch(tape[index+1:], regex[state+2:]) o. \
                       self.isMatch(tape[index:], regex[state+2:])
            ____:
                r.. self.isMatch(tape[index:], regex[state+2:])
        ____:  # without trailing *
            __ tape[index] __ regex[state] o. regex[state] __ ".":
                r.. self.isMatch(tape[index+1:], regex[state+1:])
            ____:
                r.. False

    ___ isMatch(self, s, p):
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

        m = l..(tape)
        n = l..(regex)

        dp = [[False ___ _ __ xrange(n+1)] ___ _ __ xrange(m+1)]

        # edge cases
        dp[m][n] = True
        ___ j __ xrange(n-1, -1, -1):
            __ regex[j] __ "*":
                dp[m][j] = dp[m][j+1]
            ____ j+1 < n a.. regex[j+1] __ "*":
                dp[m][j] = dp[m][j+1]
            ____:
                dp[m][j] = False

        # normal cases
        ___ i __ xrange(m-1, -1, -1):
            ___ j __ xrange(n-1, -1, -1):
                __ regex[j] __ "*":
                    __ j-1 >= 0 a.. regex[j-1] != "*":
                        dp[i][j] = dp[i][j+1]  # skip
                    ____:
                        r.. False  # two consecutive *
                ____ j+1 < n a.. regex[j+1] __ "*":
                    __ tape[i] __ regex[j] o. regex[j] __ ".":
                        dp[i][j] = dp[i][j+2] o. dp[i+1][j] o. dp[i+1][j+2]  # what is done in dfs
                    ____:
                        dp[i][j] = dp[i][j+2]
                ____:
                    __ tape[i] __ regex[j] o. regex[j] __ ".":
                        dp[i][j] = dp[i+1][j+1]
                    ____:
                        dp[i][j] = False

        # notice that in edge cases and normal cases, checking conditions are exactly the same

        r.. dp[0][0]


__ __name__ __ "__main__":
    ... Solution().isMatch("aa", "a") __ False
    ... Solution().isMatch("aa", "aa") __ True
    ... Solution().isMatch("aaa", "aa") __ False
    ... Solution().isMatch("aa", "a*") __ True
    ... Solution().isMatch("ab", ".*") __ True
    ... Solution().isMatch("aab", "c*a*b") __ True
    ... Solution().isMatch("aaa", "a*a") __ True
    ... Solution().isMatch("bbbba", ".*a*a") __ True
    ... Solution().isMatch("a", "aa*") __ True