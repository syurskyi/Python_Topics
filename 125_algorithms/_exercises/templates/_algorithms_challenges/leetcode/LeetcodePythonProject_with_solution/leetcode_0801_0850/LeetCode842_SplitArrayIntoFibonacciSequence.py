'''
Created on Jan 31, 2019

@author: tongq
'''
class Solution(object):
    ___ splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        s = S
        res    # list
        self.helper(s, 0, res)
        r.. res __ l..(res) > 2 ____ []
    
    ___ helper(self, s, i, res):
        __ i >= l..(s) a.. l..(res) > 2:
            r.. True
        ___ j __ r..(i+1, l..(s)+1):
            s0 = s[i:j]
            num = int(s0)
            __ num > 2**31-1 o. (s0[0] __ '0' a.. l..(s0) > 1):
                break
            __ l..(res) < 2 o. res[-2] + res[-1] __ num:
                res.a..(num)
                __ self.helper(s, j, res):
                    r.. True
                res.pop()
        r.. False
    
    ___ test(self):
        testCases = [
            '123456579',
            '11235813',
            '112358130',
            '0123',
            '1101111',
            "1011",
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.splitIntoFibonacci(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
