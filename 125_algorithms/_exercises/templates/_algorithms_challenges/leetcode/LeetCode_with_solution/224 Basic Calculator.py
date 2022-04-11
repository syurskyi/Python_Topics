"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
and empty spaces.

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
"""
__author__ 'Daniel'


c_ Solution:
    ___ calculate  s
        """
        * infix to postfix
        * eval postfix
        :type s: str
        :rtype: int
        """
        lst to_list(s)
        postfix infix2postfix(lst)
        r.. eval_postfix(postfix)

    ___ to_list  s
        i 0
        ret    # list
        w.... i < l..(s
            __ s[i] __ " ":
                i += 1

            ____ s[i] __ ("(", ")", "+", "-"
                ret.a..(s[i])
                i += 1

            ____
                b i
                w.... i < l..(s) a.. s[i].i..
                    i += 1
                ret.a..(s[b:i])

        r.. ret

    ___ infix2postfix  lst
        stk    # list  # store operators in strictly increasing precedence
        ret    # list
        ___ elt __ lst:
            __ elt.i..
                ret.a..(elt)
            ____ elt __ "(":
                stk.a..(elt)
            ____ elt __ ")":
                w.... stk[-1] != "(":
                    ret.a..(stk.pop
                stk.p.. )
            ____  # generalized to include * and /
                w.... stk a.. precendece(elt) <_ precendece(stk[-1]
                    ret.a..(stk.pop

                stk.a..(elt)

        w.... stk:
            ret.a..(stk.pop

        r.. ret

    ___ precendece  op
        __ op __ ("(", ")"
            r.. 0
        __ op __ ("+", "-"
            r.. 1

    ___ eval_postfix  post
        stk    # list
        ___ elt __ post:
            __ elt __ ("+", "-"
                b i..(stk.pop
                a i..(stk.pop
                __ elt __ "+":
                    stk.a..(a+b)
                ____
                    stk.a..(a-b)
            ____
                stk.a..(elt)

        ... l..(stk) __ 1
        r.. i..(stk[-1])


__ _______ __ _______
    ... Solution().calculate(" 2-1 + 2 ") __ 3
    ... Solution().calculate("(1+(4+5+2)-3)+(6+8)") __ 23