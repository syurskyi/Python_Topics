"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before
implementing one.
"""
__author__ = 'Danyang'
class Solution:
    ___ isNumber_builtin(self, s
        """
        using built-in function
        :param s: a string
        :return: boolean
        """
        try:
            float(s)
            r_ True
        except ValueError:
            r_ False

    ___ isNumber(self, s
        """
        D-FSA: Deterministic Finite State Automata
        Transition table T, which is constructed from FSA

        state = T[state, token]

        Draw the diagram for FSA
        :param s:
        :return:
        """
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        E = 5
        T = [
            [-1, 0, 3, 1, 2,-1],
            [-1, 8,-1, 1, 4, 5],
            [-1,-1,-1, 4,-1,-1],
            [-1,-1,-1, 1, 2,-1],
            [-1, 8,-1, 4,-1, 5],
            [-1,-1, 6, 7,-1,-1],
            [-1,-1,-1, 7,-1,-1],
            [-1, 8,-1, 7,-1,-1],
            [-1, 8,-1,-1,-1,-1], # 9
        ]
        state = 0
        for char in s:
            __ state__-1:
                r_ False
            __ char__" ":
                token = SPACE
            ____ char in ("-", "+"
                token = SIGN
            ____ char in map(str, range(10)):
                token = DIGIT
            ____ char__".":
                token = DOT
            ____ char in ("e", "E"
                token = E
            ____
                token = INVALID

            state = T[state][token]
        __ state in (1, 4, 7, 8  # accept state
            r_ True
        ____
            r_ False

__ __name____"__main__":
    assert Solution().isNumber(".2e81")__True
    assert Solution().isNumber("6+1")__False
    assert Solution().isNumber("1 a")__False
    assert Solution().isNumber("1e10")__True
    assert Solution().isNumber(" 0.1")__True
    assert Solution().isNumber("abc")__False


