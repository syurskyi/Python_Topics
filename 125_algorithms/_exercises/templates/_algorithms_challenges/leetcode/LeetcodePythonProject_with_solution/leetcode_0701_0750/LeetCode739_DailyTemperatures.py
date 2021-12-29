'''
Created on Mar 14, 2018

@author: tongq
'''
class Solution(object):
    ___ dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = []
        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            while stack and temperatures[stack[-1]] <= t:
                stack.pop()
            __ not stack:
                res.insert(0, 0)
            else:
                res.insert(0, stack[-1]-i)
            stack.append(i)
        return res
    
    ___ test(self):
        testCases = [
            [73, 74, 75, 71, 69, 72, 76, 73],
        ]
        for temperatures in testCases:
            print('temperatures: %s' % temperatures)
            result = self.dailyTemperatures(temperatures)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
