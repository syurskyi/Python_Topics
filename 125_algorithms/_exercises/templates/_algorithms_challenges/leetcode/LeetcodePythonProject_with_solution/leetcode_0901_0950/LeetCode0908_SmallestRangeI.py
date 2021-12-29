class Solution(object):
    ___ smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(max(A)-min(A)-2*K, 0)

    ___ smallestRangeI_own(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        minVal = min(A)
        maxVal = max(A)
        med = (minVal+maxVal) // 2
        minVal = float('inf')
        maxVal = float('-inf')
        for num in A:
            __ num > med:
                __ num - med > K:
                    num -= K
                else:
                    num = med
            elif num < med:
                __ med - num > K:
                    num += K
                else:
                    num = med
            maxVal = max(maxVal, num)
            minVal = min(minVal, num)
        return maxVal - minVal

    ___ test(self):
        testCases = [
            [[1], 0],
            [[0,10], 2],
            [[1,3,6], 3],
        ]
        for a, k in testCases:
            res = self.smallestRangeI(a, k)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ == '__main__':
    Solution().test()
