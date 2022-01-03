'''
Created on Mar 28, 2018

@author: tongq
'''
c_ Solution(object):
    ___ reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        step = 0
        sumVal = 0
        w.... sumVal < target:
            step += 1
            sumVal += step
        w.... (sumVal-target)%2 != 0:
            step += 1
            sumVal += step
        r.. step
    
    ___ test
        testCases = [
            3,
            2,
        ]
        ___ target __ testCases:
            print('target: %s' % target)
            result = reachNumber(target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
