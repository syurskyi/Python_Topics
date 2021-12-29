'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object):
    ___ largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        s = S
        res    # list
        left = 0
        ___ i __ r..(l..(s)+1):
            __ i __ l..(s) o. s[i] != s[left]:
                __ i-left >= 3:
                    res.a..([left, i-1])
                left = i
        r.. res
    
    ___ test(self):
        testCases = [
            'aaa',
            'abbxxxxzzy',
            'abc',
            'abcdddeeeeaabbbcd',
        ]
        ___ s __ testCases:
            result = self.largeGroupPositions(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
