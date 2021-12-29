'''
Created on Mar 31, 2018

@author: tongq
'''
class Solution(object):
    ___ makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        i = 0
        res    # list
        ___ j, c __ e..(S):
            count = count+1 __ c__'1' ____ count-1
            __ count __ 0:
                res.a..('1'+self.makeLargestSpecial(S[i+1:j])+'0')
                i = j+1
        r.. ''.join(s..(res, reverse=True))
    
    ___ test(self):
        testCases = [
            '11011000',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.makeLargestSpecial(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
