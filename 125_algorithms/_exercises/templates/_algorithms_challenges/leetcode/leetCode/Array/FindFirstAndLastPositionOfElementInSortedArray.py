"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

要求： 时间复杂度必须是 O(log n)

看到log n 立马先想到二分，排好序的数组，刚好可以利用二分。

正好 Python 内置模块 bisect 有写二分法，稍加改进即可使用。

一般可能会想到用递归实现，下面是 Python 官方的迭代实现：
```
初始定义两个变量：
lo (lower)
hi (higher)

lo 初始为首位 0.
hi 则为 len(list).

每次都获取 list[mid] mid = (lo + hi) // 2.

list[mid] 有三种情况：
1. 与target相等。
2. 大于target.
3. 小于target.

lo    mid hi
1 2 3 4 5 6

若mid大于target则表示要找的目标存在于 lo 与 mid之间。
     小于则表示要找的目标存在于 mid 与 hi之间。

要改进的地方在于，处理相等的情况：

在不相等时先移动lo还是hi都无所谓。
在相等时若先移动 lo 则尽可能找到的是最右边的一个。
                hi 则是最左边的一个。

lo      hi
1 2 2 2 3

先移动 lo
    lo  hi
1 2 2 2 3
  ↑
没有可能在找到它。

先移动 hi
lo  hi 
1 2 2 2 3
      ↑
    没有可能在找到它。


所以一左一右，两次二分即可。

测试地址：
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

beat
94%

```


"""

c.. Solution o..
    ___ find_right  nums, target
        lo = 0
        hi = l..(nums)
        equals   # list
        _____ lo < hi:
            mid = (lo + hi) // 2
            __ target __ nums[mid]:
                equals.append(mid)
            
            __ target < nums[mid]:
                hi = mid
            ____
                lo = mid + 1

        r_ equals[-1] __ equals else -1
    
    ___ find_left  nums, target
        lo = 0
        hi = l..(nums)
        equals   # list
        _____ lo < hi:
            mid = (lo + hi) // 2
            __ target __ nums[mid]:
                equals.append(mid)
            
            __ target > nums[mid]:
                lo = mid + 1
            ____
                hi = mid
        r_ equals[-1] __ equals else -1
            
        
    ___ searchRange  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = self.find_left(nums, target)
        __ left __ -1:
            r_ [-1, -1]
        
        r_ [left, self.find_right(nums, target)]
