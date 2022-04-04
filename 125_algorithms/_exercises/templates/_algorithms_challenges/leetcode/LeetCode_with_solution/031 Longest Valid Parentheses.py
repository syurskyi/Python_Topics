"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
__author__ = 'Danyang'


c_ Solution(o..
    ___ longestValidParentheses  s
        """
        Stack holds the index of unpaired brackets

        case 1:
        ()())), length is last_paired_index+1
        case 2:
        ))()(), length is last_paired_index - stack[-1]
        case 3:
        (())), length is last_paired_index+1
        case 4:
        ((())(, length is last_paired_index - stack[-1]
        :param s: a string
        :return: an integer
        """
        stk    # list  # hold the INDEX of UNPAIRED bracket, either ( or )
        maxa = 0
        ___ idx, val __ e..(s
            __ val __ ")" a.. stk a.. s[stk[-1]] __ "(":
                stk.p.. )
                __ n.. stk:
                    maxa = m..(maxa, idx+1)
                ____
                    maxa = m..(maxa, idx-stk[-1])
            ____
                stk.a..(idx)

        r.. maxa


__ _______ __ _______
    ... Solution().longestValidParentheses("(()()") __ 4
    ... Solution().longestValidParentheses("()(()") __ 2
    ... Solution().longestValidParentheses("(()") __ 2
    ... Solution().longestValidParentheses(")()())") __ 4