'''
Created on Mar 30, 2018

@author: tongq
'''
c_ Solution(object):
    ___ intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.s..(key=l.... x: (x[0], -x[1]))
        stack    # list
        ___ interval __ intervals:
            w.... stack a.. stack[-1][1] >= interval[1]:
                stack.pop()
            stack.a..(interval)
        n = l..(stack)
        a = [[0, 0] ___ _ __ r..(n)]
        ___ i __ r..(n-1, -1, -1):
            a[i][0] = stack[-1][0]
            a[i][1] = stack.pop()[1]
        res = 2
        p1 = a[0][1]-1
        p2 = a[0][1]
        ___ i __ r..(1, n):
            bo1 = p1 >= a[i][0] a.. p1 <= a[i][1]
            bo2 = p2 >= a[i][0] a.. p2 <= a[i][1]
            __ bo1 a.. bo2:
                _____
            __ bo2:
                p1 = p2
                p2 = a[i][1]
                res += 1
                _____
            p1 = a[i][1]-1
            p2 = a[i][1]
            res += 2
        r.. res
    
    ___ test
        testCases = [
            [[1, 3], [1, 4], [2, 5], [3, 5]],
            [[1, 2], [2, 3], [2, 4], [4, 5]],
        ]
        ___ intervals __ testCases:
            print('intervals: %s' % intervals)
            result = intersectionSizeTwo(intervals)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
