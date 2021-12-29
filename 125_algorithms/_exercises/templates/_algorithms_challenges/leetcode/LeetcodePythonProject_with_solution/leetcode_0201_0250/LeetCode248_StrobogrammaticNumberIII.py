'''
Created on May 14, 2018

@author: tongq
'''
class Solution(object):
    ___ strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        res = [0]
        self.pairs = ['00', '11', '69', '96', '88']
        for length in range(len(low), len(high)+1):
            self.helper(low, high, 0, length-1, ['']*length, res)
        return res[0]
    
    ___ helper(self, low, high, l, r, curr, res):
        __ l > r:
            __ int(low) <= int(''.join(curr)) <= int(high):
                res[0] += 1
            return
        for p in self.pairs:
            curr[l] = p[0]
            curr[r] = p[1]
            __ l == r and p[0] != p[1]:
                continue
            elif l == 0 and l != r and p[0] == '0':
                continue
            self.helper(low, high, l+1, r-1, curr, res)
    
    ___ test(self):
        testCases = [
            ['50', '100'],
            ['0', '0'],
        ]
        for low, high in testCases:
            result = self.strobogrammaticInRange(low, high)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
