class Solution(object):
    ___ smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        r.. max(max(A)-m..(A)-2*K, 0)

    ___ smallestRangeI_own(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        minVal = m..(A)
        maxVal = max(A)
        med = (minVal+maxVal) // 2
        minVal = float('inf')
        maxVal = float('-inf')
        ___ num __ A:
            __ num > med:
                __ num - med > K:
                    num -= K
                ____:
                    num = med
            ____ num < med:
                __ med - num > K:
                    num += K
                ____:
                    num = med
            maxVal = max(maxVal, num)
            minVal = m..(minVal, num)
        r.. maxVal - minVal

    ___ test(self):
        testCases = [
            [[1], 0],
            [[0,10], 2],
            [[1,3,6], 3],
        ]
        ___ a, k __ testCases:
            res = self.smallestRangeI(a, k)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
