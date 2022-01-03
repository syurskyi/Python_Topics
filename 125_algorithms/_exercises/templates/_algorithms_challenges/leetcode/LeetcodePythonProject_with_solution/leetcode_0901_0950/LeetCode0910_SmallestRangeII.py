c_ Solution(object):
    ___ smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        __ n.. A: r.. 0
        A.s..()
        res = A[-1] - A[0]
        ___ i __ r..(l..(A)-1):
            minVal = m..(A[0]+2*K, A[i+1])
            maxVal = max(A[-1], A[i]+2*K)
            res = m..(res, maxVal - minVal)
        r.. res

    ___ test
        testCases = [
            # [[1], 0],
            # [[0,10], 2],
            [[1,3,6], 3],
        ]
        ___ a, k __ testCases:
            res = smallestRangeII(a, k)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
