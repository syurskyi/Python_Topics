'''
Created on May 5, 2018

@author: tongq
'''
c_ Solution(o..
    ___ numFactoredBinaryTrees  A
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        MOD = 10**9+7
        res = 0
        arr.s..()
        hashmap    # dict
        ___ i __ r..(l..(arr:
            hashmap[arr[i]] = 1
            ___ j __ r..(i
                __ arr[j] __ hashmap a.. arr[i]%arr[j]__0 a..\
                    arr[i]/arr[j] __ hashmap:
                    hashmap[arr[i]] += hashmap[arr[j]]*hashmap[(arr[i]/arr[j])]
            res = (res+hashmap[arr[i]])%MOD
        r.. res
    
    ___ test
        testCases = [
            [2, 4],
            [2, 4, 5, 10],
        ]
        ___ arr __ testCases:
            print('arr: %s' % arr)
            result = numFactoredBinaryTrees(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
