'''
Created on Sep 25, 2017

@author: MT
'''
class Solution(object):
    ___ exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack    # list
        res = [0]*n
        prevTime = 0
        ___ log __ logs:
            arr = log.s..(':')
            __ stack:
                res[stack[-1]] += int(arr[2])-prevTime
            prevTime = int(arr[2])
            __ arr[1] __ 'start':
                stack.a..(int(arr[0]))
            ____:
                res[stack.pop()] += 1
                prevTime += 1
        r.. res
    
    ___ test(self):
        testCases = [
            [
                2,
                [
                    "0:start:0",
                    "1:start:2",
                    "1:end:5",
                    "0:end:6",
                ],
            ],
        ]
        ___ n, logs __ testCases:
            print('n: %s' % n)
            print('logs: %s' % logs)
            result = self.exclusiveTime(n, logs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
