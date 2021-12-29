class Solution(object):
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

    ___ test(self):
        testCases = [
            # [0],
            # [1, 1, 2],
            [1, 2, 4],
        ]
        ___ arr __ testCases:
            res = self.subarrayBitwiseORs(arr)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
