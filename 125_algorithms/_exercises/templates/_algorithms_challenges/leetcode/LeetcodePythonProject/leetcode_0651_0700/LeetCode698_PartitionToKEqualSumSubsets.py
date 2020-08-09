'''
Created on Oct 26, 2017

@author: MT
'''
class Solution(object
    ___ canPartitionKSubsets(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sumVal = sum(nums)
        __ sumVal%k != 0:
            r_ False
        nums.sort(reverse=True)
        r_ self.helper(nums, [0]*k, sumVal//k, 0, k)
    
    ___ helper(self, nums, elems, target, ind, k
        __ ind __ k:
            r_ True
        for i in range(le.(nums)):
            __ elems[ind]+nums[i] <= target:
                elems[ind] += nums[i]
                __ elems[ind] __ target and\
                    self.helper(nums[:i]+nums[i+1:], elems, target, ind+1, k
                    r_ True
                ____ self.helper(nums[:i]+nums[i+1:], elems, target, ind, k
                    r_ True
                elems[ind] -= nums[i]
            ____
                break
        r_ False
    
    ___ test(self
        testCases = [
            [
                [4, 3, 2, 3, 5, 2, 1],
                4,
            ],
            [
                [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908],
                4,
            ],
            [
                [4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2],
                13,
            ],
        ]
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.canPartitionKSubsets(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
