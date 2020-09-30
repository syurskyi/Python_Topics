# Longest Valid Parentheses
# Question: Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
# Solutions:


c_ Solution:
    # @param s, a string
    # @return an integer

    ___ longestValidParentheses(self, s):
        maxlen, stack, last _ 0,   # list, -1
        ___ i __ ra..(le.(s)):
            __ s[i]__'(':
                stack.ap..(i) # push the INDEX into the stack!!!!
            ____
                __ stack __   # list:
                    last _ i
                ____
                    stack.p..()
                    __ stack __   # list:
                        maxlen _ ma.(maxlen, i-last)
                    ____
                        maxlen _ ma.(maxlen, i-stack[le.(stack)-1])
        r_ maxlen


Solution().longestValidParentheses(")()())")