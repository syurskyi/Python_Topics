'''
Created on Mar 14, 2018

@author: tongq
'''
class Solution(object
    ___ dailyTemperatures(self, temperatures
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = []
        ___ i in range(le.(temperatures)-1, -1, -1
            t = temperatures[i]
            w___ stack and temperatures[stack[-1]] <= t:
                stack.p..
            __ not stack:
                res.insert(0, 0)
            ____
                res.insert(0, stack[-1]-i)
            stack.append(i)
        r_ res
    
    ___ test(self
        testCases = [
            [73, 74, 75, 71, 69, 72, 76, 73],
        ]
        ___ temperatures in testCases:
            print('temperatures: %s' % temperatures)
            result = self.dailyTemperatures(temperatures)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
