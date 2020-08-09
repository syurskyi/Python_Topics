'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object
    ___ findContentChildren(self, g, s
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        count = 0
        w___ i < le.(g) and j < le.(s
            __ g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            ____
                j += 1
        r_ count
    
    ___ test(self
        testCases = [
            ([1,2,3], [1,1]),
            ([1,2], [1,2,3]),
            ([10,9,8,7], [5,6,7,8]),
        ]
        for g, s in testCases:
            print('g: %s' % g)
            print('s: %s' % s)
            result = self.findContentChildren(g, s)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

