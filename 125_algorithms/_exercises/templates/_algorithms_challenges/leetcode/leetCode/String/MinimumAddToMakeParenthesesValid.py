"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
 

Note:

S.length <= 1000
S only consists of '(' and ')' characters.

给一个字符串只包含 "(" 和 ")"。

返回至少补多少个可以达成全部有效。

思路：
去除原来有效的，剩余多少个即为需要多少个。


"""
c.. Solution o..
    ___ minAddToMakeValid  S
        """
        :type S: str
        :rtype: int
        """
        __ n.. S:
            r_ 0
        t = [S[0]]
        ___ i __ S[1:]:
            __ i __ ')':
                __ n.. t:
                    t.append(i)
                    c_
                    
                __ t[-1] __ '(':
                    t.pop()
                ____
                    t.append(i)
            ____
                t.append(i)
        r_ l..(t)
        