'''
Created on Mar 31, 2018

@author: tongq
'''
class Solution(object
    ___ anagramMappings(self, A, B
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        arr1, arr2 = A, B
        hashmap = {}
        ___ i, num in enumerate(arr2
            __ num not in hashmap:
                hashmap[num] = []
            hashmap[num].append(i)
        res = []
        ___ num in arr1:
            res.append(hashmap[num].pop())
        r_ res
    
    ___ test(self
        testCases = [
            [
                [12, 28, 46, 32, 50],
                [50, 12, 32, 46, 28],
            ],
        ]
        ___ arr1, arr2 in testCases:
            print('arr1: %s' % arr1)
            print('arr2: %s' % arr2)
            result = self.anagramMappings(arr1, arr2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
