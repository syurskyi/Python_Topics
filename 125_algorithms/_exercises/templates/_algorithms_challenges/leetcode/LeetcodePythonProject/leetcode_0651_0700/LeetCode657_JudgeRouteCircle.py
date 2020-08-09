'''
Created on Oct 5, 2017

@author: MT
'''
class Solution(object
    ___ judgeCircle(self, moves
        """
        :type moves: str
        :rtype: bool
        """
        up, left = 0, 0
        for c in moves:
            __ c __ 'L':
                left += 1
            ____ c __ 'R':
                left -= 1
            ____ c __ 'U':
                up += 1
            ____
                up -= 1
        r_ up __ 0 and left __ 0
    
    ___ test(self
        testCases = [
            'UD',
            'LL',
        ]
        for moves in testCases:
            print('moves: %s' % moves)
            result = self.judgeCircle(moves)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
