'''
Created on Oct 2, 2017

@author: MT
'''
class Solution(object):
    ___ predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        queue1    # list
        queue2    # list
        n = l..(senate)
        ___ i __ r..(n):
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
    
    ___ test(self):
        testCases = [
            'RD',
            'RDD',
            'DDRRR',
        ]
        ___ senate __ testCases:
            print('senate: %s' % senate)
            result = self.predictPartyVictory(senate)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
