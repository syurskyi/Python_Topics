'''
Created on Apr 3, 2018

@author: tongq
'''
class Solution(object
    ___ minSwapsCouples(self, row
        """
        :type row: List[int]
        :rtype: int
        """
        hashmap = {}
        idx = 0
        res = 0
        w___ idx < le.(row
            hashmap[row[idx]] = row[idx+1]
            hashmap[row[idx+1]] = row[idx]
            idx += 2
        idx = 0
        w___ idx < le.(row
            __ hashmap[idx] != idx+1:
                nextVal = hashmap[idx+1]
                currVal = hashmap[idx]
                hashmap[currVal] = nextVal
                hashmap[nextVal] = currVal
                res += 1
            idx += 2
        r_ res
    
    ___ test(self
        testCases = [
            [0, 2, 1, 3],
            [3, 2, 0, 1],
        ]
        for row in testCases:
            print('row: %s' % row)
            result = self.minSwapsCouples(row)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
