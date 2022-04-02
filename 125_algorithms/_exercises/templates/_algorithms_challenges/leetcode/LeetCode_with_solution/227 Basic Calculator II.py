"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division
should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.


"""
__author__ = 'Daniel'


c_ Solution:
    ___ calculate  s
        """
        :type s: str
        :rtype: int
        """
        lst = p..(s)
        post = infix2postfix(lst)
        r.. eval_postfix(post)

    ___ p..  s
        """
        return tokens
        """
        i = 0
        ret    # list
        w.... i < l..(s
            __ s[i] __ " ":
                i += 1

            ____ s[i] __ ("(", ")", "+", "-", "*", "/"
                ret.a..(s[i])
                i += 1

            ____:
                b = i
                w.... i < l..(s) a.. s[i].i..
                    i += 1
                ret.a..(s[b:i])

        r.. ret

    ___ infix2postfix  lst
        # operator stacks rather than operand
        stk    # list  # stk only stores operators in strictly increasing precedence
        ret    # list
        ___ elt __ lst:
            __ elt.i..
                ret.a..(elt)
            ____ elt __ "(":
                stk.a..(elt)
            ____ elt __ ")":
                w.... stk[-1] != "(":
                    ret.a..(stk.pop
                stk.pop()
            ____:  # generalized to include * and /
                w.... stk a.. precendece(elt) <= precendece(stk[-1]
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
        __ op __ ("*", "/"
            r.. 2
        r.. 3

    ___ eval_postfix  post
        stk    # list
        ___ elt __ post:
            __ elt __ ("+", "-", "*", "/"
                b = i..(stk.pop
                a = i..(stk.pop
                __ elt __ "+":
                    stk.a..(a+b)
                ____ elt __ "-":
                    stk.a..(a-b)
                ____ elt __ "*":
                    stk.a..(a*b)
                ____:
                    stk.a..(a/b)
            ____:
                stk.a..(elt)

        ... l..(stk) __ 1
        r.. i..(stk[-1])


__ _______ __ _______
    ... Solution().calculate("3+2*2") __ 7
