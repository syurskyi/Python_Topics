'''
Created on May 2, 2018

@author: tongq
'''
class Solution(object):
    ___ shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        s, c = S, C
        arr = []
        for i, c0 in enumerate(s):
            __ c0 == c:
                arr.append(i)
        res = []
        j = 0
        for i in range(len(s)):
            __ i < arr[j]:
                val = arr[j]-i
                __ j > 0:
                    val = min(val, i-arr[j-1])
            elif i == arr[j]:
                val = 0
                __ j < len(arr)-1:
                    j += 1
            else:
                val = i-arr[j]
            res.append(val)
        return res
    
    ___ test(self):
        testCases = [
            [
                'loveleetcode', 'e',
            ],
        ]
        for s, c in testCases:
            print('s: %s' % s)
            print('c: %s' % c)
            result = self.shortestToChar(s, c)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
