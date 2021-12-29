'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    ___ findPoisonedDurationAnother(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        __ n.. timeSeries: r.. 0
        res = 0
        ___ i __ r..(1, l..(timeSeries)):
            res += m..(timeSeries[i]-timeSeries[i-1], duration)
        res += duration
        r.. res
    
    ___ findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = 0
        prev = 0
        maxTime = 0
        ___ time __ timeSeries:
            __ maxTime < time:
                result += maxTime - prev
                prev = time
            maxTime = max(maxTime, time+duration)
        result += maxTime-prev
        r.. result
    
    ___ test(self):
        testCases = [
            [
                [1, 4],
                2,
            ],
            [
                [1, 2],
                2,
            ],
        ]
        ___ timeSeries, duration __ testCases:
            print('timeSeries: %s' % timeSeries)
            print('duration: %s' % duration)
            result = self.findPoisonedDurationAnother(timeSeries, duration)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
