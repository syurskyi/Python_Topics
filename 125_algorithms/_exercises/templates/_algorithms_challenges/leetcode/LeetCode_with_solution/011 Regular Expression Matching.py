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
__author__ 'Danyang'


c_ Solution:
    ___ isMatch_error  s, p
        """
        Using FSA? It is complicated to build compared to 066 Valid Number, since you have to construct the transition
        table from the pattern

        Algorithm: simple pointer

        :param s:
        :param p:
        :return: boolean
        """
        # rename
        tape s
        regex p

        index 0
        state 0
        w.... index < l..(tape) a.. state < l..(regex
            char tape[index]
            __ state+1 < l..(regex) a.. regex[state+1] __ "*":
                __ regex[state] !_ ".":
                    __ char __ regex[state]:  # advance tape
                        w.... index < l..(tape) a.. tape[index] __ char: index += 1
                        state += 2
                    ____
                        state += 2
                ____  # .*
                    state += 2
                    __ state < l..(regex
                        __ regex[state] !_ ".":  # find until the next char in regex
                            w.... index < l..(tape) a.. tape[index] !_ regex[state]: index += 1
                        ____  # difficult part
                            count 1

                    ____
                        r.. T..
            ____  # no * appended
                __ char __ regex[state] o. regex[state] __ ".":
                    index += 1
                    state += 1
                ____
                    _____

        __ index __ l..(tape) a.. state __ l..(regex
            r.. T..
        r.. F..


    ___ isMatch_TLE  s, p
        """
        Algorithm: dfs, advancing the tape
        "." is not a problem
        "*" is the problem

        :param s:
        :param p:
        :return: boolean
        """
        # rename
        tape s
        regex p

        index 0
        state 0

        # dfs terminal condition
        __ n.. tape a.. n.. regex:
            r.. T..
        # if not s and p or s and not p:
        __ tape a.. n.. regex:  # possible "", "a*"
            r.. F..

        __ n.. tape a.. regex:
            __ state+1 < l..(regex) a.. regex[state+1] __ "*":
                r.. isMatch(tape, regex[state+2:])
            ____
                r.. F..

        __ state+1 < l..(regex) a.. regex[state+1] __ "*":
            __ tape[index] __ regex[state] o. regex[state] __ ".":  # consume tokens
                r.. isMatch(tape[index+1:], regex[state:]) o. \
                       isMatch(tape[index+1:], regex[state+2:]) o. \
                       isMatch(tape[index:], regex[state+2:])
            ____
                r.. isMatch(tape[index:], regex[state+2:])
        ____  # without trailing *
            __ tape[index] __ regex[state] o. regex[state] __ ".":
                r.. isMatch(tape[index+1:], regex[state+1:])
            ____
                r.. F..

    ___ isMatch  s, p
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
        tape s
        regex p

        m l..(tape)
        n l..(regex)

        dp [[F.. ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]

        # edge cases
        dp[m][n] T..
        ___ j __ x..(n-1, -1, -1
            __ regex[j] __ "*":
                dp[m][j] dp[m][j+1]
            ____ j+1 < n a.. regex[j+1] __ "*":
                dp[m][j] dp[m][j+1]
            ____
                dp[m][j] F..

        # normal cases
        ___ i __ x..(m-1, -1, -1
            ___ j __ x..(n-1, -1, -1
                __ regex[j] __ "*":
                    __ j-1 >_ 0 a.. regex[j-1] !_ "*":
                        dp[i][j] dp[i][j+1]  # skip
                    ____
                        r.. F..  # two consecutive *
                ____ j+1 < n a.. regex[j+1] __ "*":
                    __ tape[i] __ regex[j] o. regex[j] __ ".":
                        dp[i][j] dp[i][j+2] o. dp[i+1][j] o. dp[i+1][j+2]  # what is done in dfs
                    ____
                        dp[i][j] dp[i][j+2]
                ____
                    __ tape[i] __ regex[j] o. regex[j] __ ".":
                        dp[i][j] dp[i+1][j+1]
                    ____
                        dp[i][j] F..

        # notice that in edge cases and normal cases, checking conditions are exactly the same

        r.. dp[0][0]


__ _______ __ _______
    ... Solution().isMatch("aa", "a") __ F..
    ... Solution().isMatch("aa", "aa") __ T..
    ... Solution().isMatch("aaa", "aa") __ F..
    ... Solution().isMatch("aa", "a*") __ T..
    ... Solution().isMatch("ab", ".*") __ T..
    ... Solution().isMatch("aab", "c*a*b") __ T..
    ... Solution().isMatch("aaa", "a*a") __ T..
    ... Solution().isMatch("bbbba", ".*a*a") __ T..
    ... Solution().isMatch("a", "aa*") __ T..