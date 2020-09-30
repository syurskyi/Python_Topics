# Longest Valid Parentheses
# Question: Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
# Solutions:


class Solution:
    # @param s, a string
    # @return an integer

    ___ longestValidParentheses(self, s):
        maxlen, stack, last = 0,   # list, -1
        ___ i __ ra..(len(s)):
            if s[i]=='(':
                stack.append(i) # push the INDEX into the stack!!!!
            else:
                if stack ==   # list:
                    last = i
                else:
                    stack.pop()
                    if stack ==   # list:
                        maxlen = ma.(maxlen, i-last)
                    else:
                        maxlen = ma.(maxlen, i-stack[len(stack)-1])
        r_ maxlen


Solution().longestValidParentheses(")()())")