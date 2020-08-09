'''
Created on May 2, 2018

@author: tongq
'''
class Solution(object
    ___ shortestToChar(self, S, C
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        s, c = S, C
        arr = []
        ___ i, c0 in enumerate(s
            __ c0 __ c:
                arr.append(i)
        res = []
        j = 0
        ___ i in range(le.(s)):
            __ i < arr[j]:
                val = arr[j]-i
                __ j > 0:
                    val = min(val, i-arr[j-1])
            ____ i __ arr[j]:
                val = 0
                __ j < le.(arr)-1:
                    j += 1
            ____
                val = i-arr[j]
            res.append(val)
        r_ res
    
    ___ test(self
        testCases = [
            [
                'loveleetcode', 'e',
            ],
        ]
        ___ s, c in testCases:
            print('s: %s' % s)
            print('c: %s' % c)
            result = self.shortestToChar(s, c)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
