'''
Created on Oct 5, 2017

@author: MT
'''
class Solution(object):
    ___ judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up, left = 0, 0
        ___ c __ moves:
            __ c __ 'L':
                left += 1
            ____ c __ 'R':
                left -= 1
            ____ c __ 'U':
                up += 1
            ____:
                up -= 1
        r.. up __ 0 a.. left __ 0
    
    ___ test(self):
        testCases = [
            'UD',
            'LL',
        ]
        ___ moves __ testCases:
            print('moves: %s' % moves)
            result = self.judgeCircle(moves)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
