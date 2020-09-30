'''
Created on Oct 2, 2017

@author: MT
'''
class Solution(object
    ___ predictPartyVictory(self, senate
        """
        :type senate: str
        :rtype: str
        """
        queue1 =   # list
        queue2 =   # list
        n = le.(senate)
        ___ i __ range(n
            __ senate[i] __ 'R':
                queue1.append(i)
            ____
                queue2.append(i)
        w___ queue1 and queue2:
            r_index = queue1.pop(0)
            d_index = queue2.pop(0)
            __ r_index < d_index:
                queue1.append(r_index+n)
            ____
                queue2.append(d_index+n)
        r_ 'Radiant' __ le.(queue1) > le.(queue2) else 'Dire'
    
    ___ test(self
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

__  -n __ '__main__':
    Solution().test()
