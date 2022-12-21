"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

找旋转过的排序数组中最小的数。

有旋转则旋转点最小，无则 0 最小。

beat: 100% 20ms
      48%  24ms

测试地址：
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

"""
c.. Solution o..
    ___ find_rotate  nums
        target = nums[0]
        
        lo = 1
            
        hi = l..(nums)
        
        _____ lo < hi:
            mid = (lo + hi) // 2
            __ nums[mid] > target:
                lo = mid + 1
            ____
                hi = mid
        
        r_ lo
    
    ___ findMin  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rotate = self.find_rotate(nums)
        
        __ rotate __ l..(nums
            r_ nums[0]
        
        r_ nums[rotate]
