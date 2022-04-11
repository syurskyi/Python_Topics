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
__author__ 'Danyang'
c_ Solution:
    ___ isNumber_builtin  s
        """
        using built-in function
        :param s: a string
        :return: boolean
        """
        ___
            f__(s)
            r.. T..
        ______ V..
            r.. F..

    ___ isNumber  s
        """
        D-FSA: Deterministic Finite State Automata
        Transition table T, which is constructed from FSA

        state = T[state, token]

        Draw the diagram for FSA
        :param s:
        :return:
        """
        INVALID 0
        SPACE 1
        SIGN 2
        DIGIT 3
        DOT 4
        E 5
        T [
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
        state 0
        ___ char __ s:
            __ state__-1:
                r.. F..
            __ char__" ":
                token SPACE
            ____ char __ ("-", "+"
                token SIGN
            ____ char __ map(s.., r..(10:
                token DIGIT
            ____ char__".":
                token DOT
            ____ char __ ("e", "E"
                token E
            ____
                token INVALID

            state T[state][token]
        __ state __ (1, 4, 7, 8  # accept state
            r.. T..
        ____
            r.. F..

__ _____ __ ____
    ... Solution().isNumber(".2e81")__True
    ... Solution().isNumber("6+1")__False
    ... Solution().isNumber("1 a")__False
    ... Solution().isNumber("1e10")__True
    ... Solution().isNumber(" 0.1")__True
    ... Solution().isNumber("abc")__False


