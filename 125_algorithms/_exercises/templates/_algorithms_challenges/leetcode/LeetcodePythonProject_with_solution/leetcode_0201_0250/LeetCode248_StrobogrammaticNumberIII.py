'''
Created on May 14, 2018

@author: tongq
'''
c_ Solution(object):
    ___ strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        res = [0]
        pairs = ['00', '11', '69', '96', '88']
        ___ length __ r..(l..(low), l..(high)+1):
            helper(low, high, 0, length-1, ['']*length, res)
        r.. res[0]
    
    ___ helper(self, low, high, l, r, curr, res):
        __ l > r:
            __ int(low) <= int(''.j..(curr)) <= int(high):
                res[0] += 1
            r..
        ___ p __ pairs:
            curr[l] = p[0]
            curr[r] = p[1]
            __ l __ r a.. p[0] != p[1]:
                continue
            ____ l __ 0 a.. l != r a.. p[0] __ '0':
                continue
            helper(low, high, l+1, r-1, curr, res)
    
    ___ test
        testCases = [
            ['50', '100'],
            ['0', '0'],
        ]
        ___ low, high __ testCases:
            result = strobogrammaticInRange(low, high)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
