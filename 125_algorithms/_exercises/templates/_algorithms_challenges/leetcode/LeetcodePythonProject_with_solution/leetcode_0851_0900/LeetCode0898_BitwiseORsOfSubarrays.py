c_ Solution(object):
    ___ subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        prevSet = set()
        uniqSet = set()
        ___ num __ A:
            currSet = set()
            prevSet.add(0)
            ___ num1 __ prevSet:
                currSet.add(num | num1)
                uniqSet.add(num | num1)
            prevSet = currSet
        r.. l..(uniqSet)

    ___ test
        testCases = [
            # [0],
            # [1, 1, 2],
            [1, 2, 4],
        ]
        ___ arr __ testCases:
            res = subarrayBitwiseORs(arr)
            print('res: %s' % res)
            print('-='*30+'-')


__ _____ __ _____
    Solution().test()
