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
        res    # list
        self.helper(num, 0, target, '', 0, 0, res)
        r.. res
    
    ___ helper(self, num, pos, target, curr, evalVal, mult, res):
        __ pos __ l..(num):
            evalVal += mult
            __ target __ evalVal:
                res.a..(curr)
            r..
        ___ i __ r..(pos+1, l..(num)+1):
            __ i > pos+1 and num[pos] __ '0':
                break
            numStr = num[pos:i]
            __ pos __ 0:
                self.helper(num, i, target, numStr, 0, int(numStr), res)
            ____:
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
        ___ num, target __ testCases:
            print('num: %s' % (num))
            print('target: %s' % (target))
            result = self.addOperators(num, target)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
