'''
Created on Jan 21, 2017

@author: MT
'''

# Definition for an interval.
c_ Interval(object):
    ___ - , s=0, e=0):
        start = s
        end = e
    
    ___ __str__
        r.. '<s: %s, e: %s>' % (start, end)
    
    ___ __repr__
        r.. __str__()

c_ Solution(object):
    ___ merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        __ n.. intervals: r.. intervals
        intervals.s..(key=l.... interval: interval.start)
        result    # list
        i = 0
        w.... i < l..(intervals):
            curr = intervals[i]
            nextEnd = curr.end
            j = i+1
            w.... j < l..(intervals):
                __ intervals[j].start > nextEnd:
                    break
                ____:
                    nextEnd = max(intervals[j].end, nextEnd)
                j += 1
            i = j
            result.a..(Interval(curr.start, nextEnd))
        
        r.. result
    
    ___ test
        testCases = [
            [[1,3],[2,6],[8,10],[15,18]],
            [[1,4],[2,3]],
        ]
        ___ intervals __ testCases:
            intervals = [Interval(x[0], x[1]) ___ x __ intervals]
            print('intervals: %s' % (intervals))
            result = merge(intervals)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
    