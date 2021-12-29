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
        for i, c in enumerate(s):
            __ c in hashmap:
                l = hashmap[c]
            else:
                l = []
            l.append(i)
            hashmap[c] = l
        sumVal = 0
        for c, l in hashmap.items():
            for i in range(len(l)):
                __ i == 0:
                    left = l[i]
                else:
                    left = l[i]-l[i-1]-1
                __ i == len(l)-1:
                    right = len(s)-l[i]-1
                else:
                    right = l[i+1]-l[i]-1
                sumVal = (sumVal+1+left+right+left*right)%(10**9+7)
        return sumVal
    
    ___ test(self):
        testCases = [
            'ABC',
            'ABA',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.uniqueLetterString(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
