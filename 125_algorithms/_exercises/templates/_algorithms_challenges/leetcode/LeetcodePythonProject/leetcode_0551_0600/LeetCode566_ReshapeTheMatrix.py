'''
Created on Aug 30, 2017

@author: MT
'''
class Solution(object
    ___ matrixReshape(self, nums, r, c
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        __ not nums or not nums[0]: r_ nums
        m, n = le.(nums), le.(nums[0])
        __ m*n != r*c:
            r_ nums
        res = []
        k, l = 0, 0
        ___ _ in range(r
            cur = []
            ___ _ in range(c
                cur.append(nums[k][l])
                l += 1
                __ l __ n:
                    l = 0
                    k += 1
            res.append(cur)
        r_ res
    
    ___ test(self
        testCases = [
            [
                [[1, 2],
                 [3, 4]],
                1,
                4,
            ],
            [
                [[1, 2],
                 [3, 4]],
                2,
                4,
            ],
        ]
        ___ nums, r, c in testCases:
            print('nums:')
            print('\n'.join([str(row) ___ row in nums]))
            print('r: %s' % r)
            print('c: %s' % c)
            result = self.matrixReshape(nums, r, c)
            print('result:')
            print('\n'.join([str(row) ___ row in result]))
            print('-='*30)

__ __name__ __ '__main__':
    Solution().test()
