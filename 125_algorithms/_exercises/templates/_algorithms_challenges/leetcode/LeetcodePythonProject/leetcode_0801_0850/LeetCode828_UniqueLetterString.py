'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object
    ___ uniqueLetterString(self, S
        """
        :type S: str
        :rtype: int
        """
        s = S
        hashmap = {}
        ___ i, c in enumerate(s
            __ c in hashmap:
                l = hashmap[c]
            ____
                l = []
            l.append(i)
            hashmap[c] = l
        sumVal = 0
        ___ c, l in hashmap.items(
            ___ i in range(le.(l)):
                __ i __ 0:
                    left = l[i]
                ____
                    left = l[i]-l[i-1]-1
                __ i __ le.(l)-1:
                    right = le.(s)-l[i]-1
                ____
                    right = l[i+1]-l[i]-1
                sumVal = (sumVal+1+left+right+left*right)%(10**9+7)
        r_ sumVal
    
    ___ test(self
        testCases = [
            'ABC',
            'ABA',
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.uniqueLetterString(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
