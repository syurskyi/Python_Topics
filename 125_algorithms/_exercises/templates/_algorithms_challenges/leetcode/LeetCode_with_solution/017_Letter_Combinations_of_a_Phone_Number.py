# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
dmap = {'2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' ',
        N..: N..}

c_ Solution o..
    ___ letterCombinations  digits):
        # DFS
        result = []
        ls = l.. digits)
        __ ls __ 0:
            r_ result
        current = digits[0]
        posfix = letterCombinations(digits[1:])
        ___ t __ dmap[current]:
            __ l.. posfix) > 0:
                ___ p __ posfix:
                    temp = t + p
                    result.append(temp)
            ____
                result.append(t)
        r_ result


