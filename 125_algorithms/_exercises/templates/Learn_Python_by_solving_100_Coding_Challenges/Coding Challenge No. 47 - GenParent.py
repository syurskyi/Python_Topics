# Generate Parentheses
# Question: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Solutions:

c_ Solution:
    # @param an integer
    # @return a list of string
    ___ helpler(, l, r, item, res):
        __ r < l:
            r_
        __ l __ 0 an. r __ 0:
            res.ap..(item)
        __ l > 0:
            helpler(l - 1, r, item + '(', res)
        __ r > 0:
            helpler(l, r - 1, item + ')', res)

    ___ generateParenthesis(, n):
        __ n __ 0:
            r_   # list
        res _   # list
        helpler(n, n, '', res)
        r_ res


Solution().generateParenthesis(3)