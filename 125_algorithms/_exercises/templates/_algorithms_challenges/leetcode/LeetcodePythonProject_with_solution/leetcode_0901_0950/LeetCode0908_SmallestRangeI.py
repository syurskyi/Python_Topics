c_ Solution(o..
    ___ smallestRangeI  A, K
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        r.. m..(m..(A)-m..(A)-2*K, 0)

    ___ smallestRangeI_own  A, K
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        minVal = m..(A)
        maxVal = m..(A)
        med = (minVal+maxVal) // 2
        minVal = f__('inf')
        maxVal = f__('-inf')
        ___ num __ A:
            __ num > med:
                __ num - med > K:
                    num -_ K
                ____
                    num = med
            ____ num < med:
                __ med - num > K:
                    num += K
                ____
                    num = med
            maxVal = m..(maxVal, num)
            minVal = m..(minVal, num)
        r.. maxVal - minVal

    ___ test
        testCases = [
            [[1], 0],
            [[0,10], 2],
            [[1,3,6], 3],
        ]
        ___ a, k __ testCases:
            res = smallestRangeI(a, k)
            print('res: %s' % res)
            print('-='*30+'-')


__ _____ __ _____
    Solution().test()
