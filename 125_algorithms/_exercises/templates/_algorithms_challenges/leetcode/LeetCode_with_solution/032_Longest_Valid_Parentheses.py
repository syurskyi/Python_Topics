import pdb
c_ Solution o..
    # def longestValidParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     ls = len(s)
    #     start = [0] * (ls + 1)
    #     all = [0] * (ls + 1)
    #     for i in reversed(range(ls - 1)):
    #         if s[i] == '(':
    #             if s[i + 1] == ')':
    #                 start[i] = 2
    #             if start[i + 1] + i + 1 < ls and s[start[i + 1] + i + 1] == ')':
    #                 start[i] = 2 + start[i + 1]
    #             if start[start[i] + i] > 0:
    #                 start[i] += start[start[i] + i]
    #         all[i] = max(start[i], all[i + 1])
    #     return all[0]

    ___ longestValidParentheses  s
        # https://leetcode.com/discuss/87988/my-easy-o-n-java-solution-with-explanation
        ls = l.. s)
        stack =    # list
        data = [0] * ls
        ___ i __ r.. ls
            curr = s[i]
            __ curr __ '(':
                stack.a.. i)
            ____
                __ l.. stack) > 0:
                    data[i] = 1
                    data[stack.pop(-1)] = 1
        tep, res = 0, 0
        ___ t __ data:
            __ t __ 1:
                tep += 1
            ____
                res = m..(tep, res)
                tep = 0
        r_ m..(tep, res)

__ ____ __ ____
    s  ?
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    print s.longestValidParentheses(')()())')
