'''
Created on Oct 2, 2017

@author: MT
'''
c_ Solution(o..
    ___ predictPartyVictory  senate
        """
        :type senate: str
        :rtype: str
        """
        queue1    # list
        queue2    # list
        n = l..(senate)
        ___ i __ r..(n
            __ senate[i] __ 'R':
                queue1.a..(i)
            ____:
                queue2.a..(i)
        w.... queue1 a.. queue2:
            r_index = queue1.pop(0)
            d_index = queue2.pop(0)
            __ r_index < d_index:
                queue1.a..(r_index+n)
            ____:
                queue2.a..(d_index+n)
        r.. 'Radiant' __ l..(queue1) > l..(queue2) ____ 'Dire'
    
    ___ test
        testCases = [
            'RD',
            'RDD',
            'DDRRR',
        ]
        ___ senate __ testCases:
            print('senate: %s' % senate)
            result = predictPartyVictory(senate)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
