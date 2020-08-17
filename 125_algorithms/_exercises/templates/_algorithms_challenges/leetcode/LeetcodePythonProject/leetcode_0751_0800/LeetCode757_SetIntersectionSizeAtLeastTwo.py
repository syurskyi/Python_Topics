'''
Created on Mar 30, 2018

@author: tongq
'''
class Solution(object
    ___ intersectionSizeTwo(self, intervals
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        ___ interval in intervals:
            w___ stack and stack[-1][1] >= interval[1]:
                stack.p..
            stack.append(interval)
        n = le.(stack)
        a = [[0, 0] ___ _ in range(n)]
        ___ i in range(n-1, -1, -1
            a[i][0] = stack[-1][0]
            a[i][1] = stack.p..[1]
        res = 2
        p1 = a[0][1]-1
        p2 = a[0][1]
        ___ i in range(1, n
            bo1 = p1 >= a[i][0] and p1 <= a[i][1]
            bo2 = p2 >= a[i][0] and p2 <= a[i][1]
            __ bo1 and bo2:
                continue
            __ bo2:
                p1 = p2
                p2 = a[i][1]
                res += 1
                continue
            p1 = a[i][1]-1
            p2 = a[i][1]
            res += 2
        r_ res
    
    ___ test(self
        testCases = [
            [[1, 3], [1, 4], [2, 5], [3, 5]],
            [[1, 2], [2, 3], [2, 4], [4, 5]],
        ]
        ___ intervals in testCases:
            print('intervals: %s' % intervals)
            result = self.intersectionSizeTwo(intervals)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
