"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

用栈即可。

测试地址：
https://leetcode.com/problems/valid-parentheses/description/

beat 85%.

"""

c.. Solution o..
    ___ isValid  s
        """
        :type s: str
        :rtype: bool
        """
        left = "({["
        left_key = {')': '(', ']': '[', '}': '{'}
        
        stack   # list
        
        ___ i __ s:
            __ i __ left:
                stack.a.. i)
            ____
                try:
                    __ stack[-1] __ left_key[i]:
                        stack.pop()
                    ____
                        r_ False
                except:
                    r_ False

        __ stack:
            r_ False
        r_ True
