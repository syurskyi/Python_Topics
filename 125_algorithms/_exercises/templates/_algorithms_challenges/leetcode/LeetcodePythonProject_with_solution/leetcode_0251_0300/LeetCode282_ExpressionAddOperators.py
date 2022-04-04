'''
Created on Mar 6, 2017

@author: MT
'''
c_ Solution(o..
    ___ addOperators  num, target
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res    # list
        helper(num, 0, target, '', 0, 0, res)
        r.. res
    
    ___ helper  num, pos, target, curr, evalVal, mult, res
        __ pos __ l..(num
            evalVal += mult
            __ target __ evalVal:
                res.a..(curr)
            r..
        ___ i __ r..(pos+1, l..(num)+1
            __ i > pos+1 a.. num[pos] __ '0':
                _____
            numStr = num[pos:i]
            __ pos __ 0:
                helper(num, i, target, numStr, 0, i..(numStr), res)
            ____
                helper(num, i, target, curr+'+'+numStr, evalVal+mult, i..(numStr), res)
                helper(num, i, target, curr+'-'+numStr, evalVal+mult, -i..(numStr), res)
                helper(num, i, target, curr+'*'+numStr, evalVal, mult*i..(numStr), res)
    
    ___ test
        testCases = [
            ('123', 6),
            ('232', 8),
            ('105', 5),
            ('00', 0),
            ('3456237490', 9191),
        ]
        ___ num, target __ testCases:
            print('num: %s' % (num
            print('target: %s' % (target
            result = addOperators(num, target)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
