'''
Created on Mar 28, 2018

@author: tongq
'''
class Solution(object
    ___ reachNumber(self, target
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        step = 0
        sumVal = 0
        w___ sumVal < target:
            step += 1
            sumVal += step
        w___ (sumVal-target)%2 != 0:
            step += 1
            sumVal += step
        r_ step
    
    ___ test(self
        testCases = [
            3,
            2,
        ]
        for target in testCases:
            print('target: %s' % target)
            result = self.reachNumber(target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
