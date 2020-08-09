'''
Created on Jan 31, 2019

@author: tongq
'''
class Solution(object
    ___ splitIntoFibonacci(self, S
        """
        :type S: str
        :rtype: List[int]
        """
        s = S
        res = []
        self.helper(s, 0, res)
        r_ res __ le.(res) > 2 else []
    
    ___ helper(self, s, i, res
        __ i >= le.(s) and le.(res) > 2:
            r_ True
        ___ j in range(i+1, le.(s)+1
            s0 = s[i:j]
            num = int(s0)
            __ num > 2**31-1 or (s0[0] __ '0' and le.(s0) > 1
                break
            __ le.(res) < 2 or res[-2] + res[-1] __ num:
                res.append(num)
                __ self.helper(s, j, res
                    r_ True
                res.pop()
        r_ False
    
    ___ test(self
        testCases = [
            '123456579',
            '11235813',
            '112358130',
            '0123',
            '1101111',
            "1011",
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.splitIntoFibonacci(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
