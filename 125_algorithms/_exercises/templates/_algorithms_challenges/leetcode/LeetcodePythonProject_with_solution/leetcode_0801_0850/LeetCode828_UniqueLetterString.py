'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object):
    ___ uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        s = S
        hashmap = {}
        ___ i, c __ enumerate(s):
            __ c __ hashmap:
                l = hashmap[c]
            ____:
                l    # list
            l.a..(i)
            hashmap[c] = l
        sumVal = 0
        ___ c, l __ hashmap.items():
            ___ i __ r..(l..(l)):
                __ i __ 0:
                    left = l[i]
                ____:
                    left = l[i]-l[i-1]-1
                __ i __ l..(l)-1:
                    right = l..(s)-l[i]-1
                ____:
                    right = l[i+1]-l[i]-1
                sumVal = (sumVal+1+left+right+left*right)%(10**9+7)
        r.. sumVal
    
    ___ test(self):
        testCases = [
            'ABC',
            'ABA',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.uniqueLetterString(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
