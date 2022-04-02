'''
Created on Apr 3, 2018

@author: tongq
'''
c_ Solution(o..
    ___ minSwapsCouples  row
        """
        :type row: List[int]
        :rtype: int
        """
        hashmap    # dict
        idx = 0
        res = 0
        w.... idx < l..(row
            hashmap[row[idx]] = row[idx+1]
            hashmap[row[idx+1]] = row[idx]
            idx += 2
        idx = 0
        w.... idx < l..(row
            __ hashmap[idx] != idx+1:
                nextVal = hashmap[idx+1]
                currVal = hashmap[idx]
                hashmap[currVal] = nextVal
                hashmap[nextVal] = currVal
                res += 1
            idx += 2
        r.. res
    
    ___ test
        testCases = [
            [0, 2, 1, 3],
            [3, 2, 0, 1],
        ]
        ___ row __ testCases:
            print('row: %s' % row)
            result = minSwapsCouples(row)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
