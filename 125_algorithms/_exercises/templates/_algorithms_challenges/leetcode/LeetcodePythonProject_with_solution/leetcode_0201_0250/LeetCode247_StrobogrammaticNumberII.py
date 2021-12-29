'''
Created on Feb 28, 2017

@author: MT
'''

class Solution(object):
    ___ findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.pairs = ['00', '11', '69', '96', '88']
        res    # list
        self.helper(0, n-1, ['']*n, res)
        r.. res
    
    ___ helper(self, l, r, curr, res):
        __ l > r:
            res.a..(''.join(curr))
            r..
        ___ p __ self.pairs:
            curr[l] = p[0]
            curr[r] = p[1]
            __ l __ r and p[0] != p[1]:
                continue
            ____ l __ 0 and l != r and p[0] __ '0':
                continue
            self.helper(l+1, r-1, curr, res)
    
    ___ findStrobogrammatic_short(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        evenMidCandidate = ['11', '69', '88', '96', '00']
        oddMidCandidate = ['0', '1', '8']
        __ n __ 1:
            r.. oddMidCandidate
        __ n __ 2:
            r.. evenMidCandidate[:-1]
        __ n % 2 != 0:
            pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
        ____:
            pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
        premid = int((n-1)/2)
        result    # list
        ___ c __ midCandidate:
            ___ p __ pre:
                result.a..(p[:premid]+c+p[premid:])
        r.. result
    
    ___ test(self):
        testCases = [
            4,
        ]
        ___ n __ testCases:
            print('n: %s' % (n))
            result = self.findStrobogrammatic(n)
            print('result: %s' % (result))
            print('-='*20+'-')
 
__ __name__ __ '__main__':
    Solution().test()
