'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object
    ___ numFactoredBinaryTrees(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        MOD = 10**9+7
        res = 0
        arr.sort()
        hashmap = {}
        ___ i in range(le.(arr)):
            hashmap[arr[i]] = 1
            ___ j in range(i
                __ arr[j] in hashmap and arr[i]%arr[j]__0 and\
                    arr[i]/arr[j] in hashmap:
                    hashmap[arr[i]] += hashmap[arr[j]]*hashmap[(arr[i]/arr[j])]
            res = (res+hashmap[arr[i]])%MOD
        r_ res
    
    ___ test(self
        testCases = [
            [2, 4],
            [2, 4, 5, 10],
        ]
        ___ arr in testCases:
            print('arr: %s' % arr)
            result = self.numFactoredBinaryTrees(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
