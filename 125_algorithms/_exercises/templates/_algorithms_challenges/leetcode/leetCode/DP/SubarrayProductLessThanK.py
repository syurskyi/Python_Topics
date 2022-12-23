"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

思路 Dp，处理下 1 即可。 不考虑 0，nums[i] 不会为 0。

beat 19%

测试地址:
https://leetcode.com/problems/subarray-product-less-than-k/description/

可剪枝优化。
"""
c.. Solution o..
    ___ numSubarrayProductLessThanK  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        dp   # list
        result = 0
        start = 0
        ___ i __ r..(l..(nums)):
            __ nums[i] < k:
                result += 1
                dp = [nums[i]]
                start = i
                ______
        
        ___ i __ r..(start+1, l..(nums)):
            __ nums[i] __ 1 a.. nums[i] < k:
                dp.a.. 1)
                result += l..(dp)
                c_
                
            new   # list
            
            __ nums[i] < k:
                result += 1
                new.a.. nums[i])
                
            
            ___ j __ dp:
                __ j * nums[i] < k:
                    result += 1
                    new.a.. j * nums[i])
            
            dp = new
        r_ result
        