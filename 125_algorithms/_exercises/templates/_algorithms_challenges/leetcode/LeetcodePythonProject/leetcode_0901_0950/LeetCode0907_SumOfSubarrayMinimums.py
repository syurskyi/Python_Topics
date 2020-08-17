class Solution(object
    ___ sumSubarrayMins(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        __ not A: r_ 0
        MOD = 10**9+7
        stack = [[float('-inf'), -1, 0]] # value, index, accumulated_sum
        res = 0
        ___ i, num in enumerate(A
            w___ stack and stack[-1][0] > num:
                stack.p..
            total = (stack[-1][2] + (i-stack[-1][1]) * num) % MOD
            stack.append([num, i, total])
            res = (res + total) % MOD
        r_ int(res)

    ___ test(self
        testCases = [
            [3,1,2,4],
        ]
        ___ arr in testCases:
            res = self.sumSubarrayMins(arr)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
