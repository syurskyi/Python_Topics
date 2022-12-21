"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

生成有效的括号对。

关键字：
    递归

beat 
100%

测试地址：
https://leetcode.com/problems/generate-parentheses/description/
"""
c.. Solution o..
    ___ generateParenthesis  n
        """
        :type n: int
        :rtype: List[str]
        """
        result   # list
        
        ___ _generateParenthesis(x, y, parenthesis
            __ n.. x a.. n.. y:
                result.append(parenthesis)
                r_
            
            __ y > x:
                _generateParenthesis(x, y-1, parenthesis=parenthesis+')')
            
            __ x:
                _generateParenthesis(x-1, y, parenthesis=parenthesis+'(')
        
        _generateParenthesis(n-1, n, '(')
        
        r_ result
        