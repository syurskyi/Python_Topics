c_ Solution(object):
    ___ sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        __ n.. A: r.. 0
        MOD = 10**9+7
        stack = [[float('-inf'), -1, 0]] # value, index, accumulated_sum
        res = 0
        ___ i, num __ e..(A):
            w.... stack a.. stack[-1][0] > num:
                stack.pop()
            total = (stack[-1][2] + (i-stack[-1][1]) * num) % MOD
            stack.a..([num, i, total])
            res = (res + total) % MOD
        r.. i..(res)

    ___ test
        testCases = [
            [3,1,2,4],
        ]
        ___ arr __ testCases:
            res = sumSubarrayMins(arr)
            print('res: %s' % res)
            print('-='*30+'-')


__ _____ __ _____
    Solution().test()
