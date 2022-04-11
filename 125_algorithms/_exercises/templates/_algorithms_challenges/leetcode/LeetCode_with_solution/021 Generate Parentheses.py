"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
__author__ 'Danyang'
c_ Solution:
    ___ generateParenthesis  n
        """
        :param n: integer
        :return: list of string
        """
        result    # list
        generateParenthesisDfs(result, "", n, n)
        r.. result

    ___ generateParenthesisDfs  result, cur, left, right
        """
        DFS
        Catalan Number
        :param result: result list
        :param cur: currently processing string
        :param left: number of left parenthesis remaining
        :param right: number of right parenthesis remaining
        """
        __ left __ 0 a.. right __ 0:
            result.a..(cur)
            r..

        # add left parenthesis
        __ left > 0:
            generateParenthesisDfs(result, cur + "(", left - 1, right)
        # add right parenthesis
        __ right > left:
            generateParenthesisDfs(result, cur + ")", left, right - 1)


__ _____ __ ____
    ... Solution().generateParenthesis(3)__ '((()))', '(()())', '(())()', '()(())', '()()()'
