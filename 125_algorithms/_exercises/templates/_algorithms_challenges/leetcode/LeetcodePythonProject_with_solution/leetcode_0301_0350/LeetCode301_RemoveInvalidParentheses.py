'''
Created on Mar 11, 2017

@author: MT
'''

class Solution(object):
    ___ removeInvalidParentheses(self, s):
        rmL, rmR = 0, 0
        for c in s:
            __ c == '(':
                rmL += 1
            elif c == ')':
                __ rmL > 0:
                    rmL -= 1
                else:
                    rmR += 1
        result = set()
        self.helper(s, 0, result, '', rmL, rmR, 0)
        return list(result)
    
    ___ helper(self, s, i, result, elem, rmL, rmR, openNum):
        __ rmL < 0 or rmR < 0 or openNum < 0:
            return
        __ i == len(s):
            __ rmL == 0 and rmR == 0 and openNum == 0:
                result.add(elem)
            return
        c = s[i]
        __ c == '(':
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum+1)
            self.helper(s, i+1, result, elem, rmL-1, rmR, openNum)
        elif c == ')':
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum-1)
            self.helper(s, i+1, result, elem, rmL, rmR-1, openNum)
        else:
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum)
    
    ___ test(self):
        testCases = [
            '()())()',
            '(a)())()',
            ')(',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.removeInvalidParentheses(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ == '__main__':
    Solution().test()
