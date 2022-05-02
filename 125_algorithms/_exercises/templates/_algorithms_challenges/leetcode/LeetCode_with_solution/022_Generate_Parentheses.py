# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
c_ Solution o..
    ___ generateParenthesis  n):
        __ n __ 1:
            r_ ['()']
        last_list = generateParenthesis(n - 1)
        res =    # list
        ___ t __ last_list:
            curr = t + ')'
            ___ index __ r.. l.. curr)):
                __ curr[index] __ ')':
                    res.append(curr[:index] + '(' + curr[index:])
        r_ list(set(res))


    # def generateParenthesis(self, n):
    #     def generate(leftnum, rightnum, s, result):
    #         if leftnum == 0 and rightnum == 0:
    #             result.append(s)
    #         if leftnum > 0:
    #             generate(leftnum - 1, rightnum, s + '(', result)
    #         if rightnum > 0 and leftnum < rightnum:
    #             generate(leftnum, rightnum - 1, s + ')', result)
    #
    #     result = []
    #     s = ''
    #     generate(n, n, s, result)
    #     return result
