'''
Created on Jan 21, 2017

@author: MT
'''

# Definition for an interval.
class Interval(object):
    ___ __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    ___ __str__(self):
        r.. '<s: %s, e: %s>' % (self.start, self.end)
    
    ___ __repr__(self):
        r.. self.__str__()

class Solution(object):
    ___ merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        __ n.. intervals: r.. intervals
        intervals.sort(key=l.... interval: interval.start)
        result    # list
        i = 0
        while i < l..(intervals):
            curr = intervals[i]
            nextEnd = curr.end
            j = i+1
            while j < l..(intervals):
                __ intervals[j].start > nextEnd:
                    break
                ____:
                    nextEnd = max(intervals[j].end, nextEnd)
                j += 1
            i = j
            result.a..(Interval(curr.start, nextEnd))
        
        r.. result
    
    ___ test(self):
        testCases = [
            [[1,3],[2,6],[8,10],[15,18]],
            [[1,4],[2,3]],
        ]
        ___ intervals __ testCases:
            intervals = [Interval(x[0], x[1]) ___ x __ intervals]
            print('intervals: %s' % (intervals))
            result = self.merge(intervals)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
    