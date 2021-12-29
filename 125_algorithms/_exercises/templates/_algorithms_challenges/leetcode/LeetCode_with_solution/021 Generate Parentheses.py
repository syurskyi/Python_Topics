"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
__author__ = 'Danyang'
class Solution:
    ___ generateParenthesis(self, n):
        """
        :param n: integer
        :return: list of string
        """
        result    # list
        self.generateParenthesisDfs(result, "", n, n)
        r.. result

    ___ generateParenthesisDfs(self, result, cur, left, right):
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
            self.generateParenthesisDfs(result, cur + "(", left - 1, right)
        # add right parenthesis
        __ right > left:
            self.generateParenthesisDfs(result, cur + ")", left, right - 1)


__ __name____"__main__":
    ... Solution().generateParenthesis(3)__['((()))', '(()())', '(())()', '()(())', '()()()']
