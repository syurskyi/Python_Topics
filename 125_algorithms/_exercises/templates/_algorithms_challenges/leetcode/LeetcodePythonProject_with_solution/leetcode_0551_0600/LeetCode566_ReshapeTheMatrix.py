'''
Created on Aug 30, 2017

@author: MT
'''
class Solution(object):
    ___ matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        __ n.. nums o. n.. nums[0]: r.. nums
        m, n = l..(nums), l..(nums[0])
        __ m*n != r*c:
            r.. nums
        res    # list
        k, l = 0, 0
        ___ _ __ r..(r):
            cur    # list
            ___ _ __ r..(c):
                cur.a..(nums[k][l])
                l += 1
                __ l __ n:
                    l = 0
                    k += 1
            res.a..(cur)
        r.. res
    
    ___ test(self):
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
        ___ nums, r, c __ testCases:
            print('nums:')
            print('\n'.join([s..(row) ___ row __ nums]))
            print('r: %s' % r)
            print('c: %s' % c)
            result = self.matrixReshape(nums, r, c)
            print('result:')
            print('\n'.join([s..(row) ___ row __ result]))
            print('-='*30)

__ __name__ __ '__main__':
    Solution().test()
