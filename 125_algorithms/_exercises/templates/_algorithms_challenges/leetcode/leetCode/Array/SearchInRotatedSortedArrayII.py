"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

search in rotated sorted array 变形版本：

与之前的区别是有重复，重复的值会造成什么样的影响呢？

1, 1, 1, 1, 1, 1, 2, 1, 1

在这个例子中

旋转的点是 1, 如果再用之前的方法，nums[0] 是没办法保证比旋转的点之后的元素都大的，
循环之后的mid是1，不大于nums[0] 不大于 mid 的情况中会把hi变为mid这样就会造成之后的数据丢失。
其他的情况可以与 I 一样。

我想到的解决方法：
1. 可以把与 nums[0] 相同的一直吞并。 这里用的方法是一直迭代。

总时间复杂度的话最差会有 O(n + log n)。

测试地址：
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

beat 89% 24ms

平均24 - 28 ms。

"""
c.. Solution o..
    ___ find_rotate  nums
        target = nums[0]
        lo = 1

        ___ i __ r..(1, l..(nums)):
            __ nums[i] __ target:
                lo += 1
            ____
                break
    
        hi = l..(nums)
        
        _____ lo < hi:
            mid = (lo + hi) // 2
            __ nums[mid] > target:
                lo = mid + 1
            ____
                hi = mid
        
        r_ lo
        
    ___ bi_search  nums, target, lo, hi
        _____ lo < hi:
            mid = (lo + hi) // 2
            __ nums[mid] __ target:
                r_ mid
            
            __ nums[mid] > target:
                hi = mid
            ____
                lo = mid + 1
        
        r_ -1
    
        
    ___ search  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ n.. nums:
            r_ False
        
        rotate_index = self.find_rotate(nums)
        
        lo = 0
        hi = rotate_index

        one = self.bi_search(nums, target, lo, hi)
        __ one != -1:
            r_ True
        
        two = self.bi_search(nums, target, hi, l..(nums))
        __ two != -1:
            r_ True
        r_ False
