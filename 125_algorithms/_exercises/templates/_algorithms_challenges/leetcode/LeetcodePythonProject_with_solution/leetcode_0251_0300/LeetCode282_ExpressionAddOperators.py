'''
Created on Mar 6, 2017

@author: MT
'''
class Solution(object):
    ___ addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.helper(num, 0, target, '', 0, 0, res)
        return res
    
    ___ helper(self, num, pos, target, curr, evalVal, mult, res):
        __ pos == len(num):
            evalVal += mult
            __ target == evalVal:
                res.append(curr)
            return
        for i in range(pos+1, len(num)+1):
            __ i > pos+1 and num[pos] == '0':
                break
            numStr = num[pos:i]
            __ pos == 0:
                self.helper(num, i, target, numStr, 0, int(numStr), res)
            else:
                self.helper(num, i, target, curr+'+'+numStr, evalVal+mult, int(numStr), res)
                self.helper(num, i, target, curr+'-'+numStr, evalVal+mult, -int(numStr), res)
                self.helper(num, i, target, curr+'*'+numStr, evalVal, mult*int(numStr), res)
    
    ___ test(self):
        testCases = [
            ('123', 6),
            ('232', 8),
            ('105', 5),
            ('00', 0),
            ('3456237490', 9191),
        ]
        for num, target in testCases:
            print('num: %s' % (num))
            print('target: %s' % (target))
            result = self.addOperators(num, target)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
