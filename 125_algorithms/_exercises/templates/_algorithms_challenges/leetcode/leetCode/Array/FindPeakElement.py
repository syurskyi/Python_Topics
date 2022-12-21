"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

log n待续。

先O(n)。

看来测试数据不多，O(n) 的可以 beat 100%.

测试地址：
https://leetcode.com/problems/find-peak-element/description/

"""
c.. Solution o..
    ___ findPeakElement  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = l..(nums)
        
        ___ i __ r..(1, length-1
            __ nums[i-1] < nums[i] > nums[i+1]:
                r_ i
        
        __ length <= 2:
            r_ nums.index(m..(nums))
        ____
            __ nums[0] > nums[1]:
                r_ 0
            ____ nums[-1] > nums[-2]:
                r_ length-1
            r_ None
