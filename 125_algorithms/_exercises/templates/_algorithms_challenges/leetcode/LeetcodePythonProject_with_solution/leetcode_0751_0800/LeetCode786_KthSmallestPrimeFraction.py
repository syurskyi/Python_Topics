'''
Created on Apr 10, 2018

@author: tongq
'''
c_ Solution(object):
    ___ kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # Use Java PriorityQueue comparator
        pass
    
    ___ test
        testCases = [
            [ [1, 2, 3, 5], 3 ],
            [ [1, 7], 1 ],
        ]
        ___ arr, k __ testCases:
            print('arr: %s' % arr)
            print('k: %s' % k)
            result = kthSmallestPrimeFraction(arr, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
