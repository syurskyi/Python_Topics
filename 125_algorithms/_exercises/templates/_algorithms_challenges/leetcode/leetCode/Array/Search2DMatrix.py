"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

给一个2d数组，给一个数字，找是否存在于其中。

思路：
两个二分法：
一个竖着的二分法，
一个横着的二分法。
竖着的二分法返回下标，横着的返回是否存在。

竖着的：

处理仅有一个的情况：
<= 都返回len()-1也就是下标
> 返回 -1 表示不存在。
其他情况下寻找 left <= x <= right.
由于 right一定大于left。所以left <= 可以放在一起判断，返回的是基础下标+当前二分的len()-1。
right == 的情况则不-1。

横着的没啥好说的，普通二分法即可。

最差是O(logm + logn)两次二分法的耗时。
beat 100%.
测试用例：
https://leetcode.com/problems/search-a-2d-matrix/description/



"""
c.. Solution o..
    ___ binarySearch  rawList, target, index=0

        __ target >= rawList[-1]:
            r_ l..(rawList) - 1

        __ target < rawList[0]:
            r_ -1

        split = l..(rawList) // 2
        
        leftList = rawList[:split]
        rightList = rawList[split:]


        __ leftList[-1] <= target a.. rightList[0] > target:
            r_ l..(leftList) + index - 1

        __ rightList[0] __ target:
            r_ l..(leftList) + index

        __ leftList[-1] > target:
            r_ self.binarySearch(leftList, target, index=index)

        __ rightList[0] < target:
            r_ self.binarySearch(rightList, target, index=index+l..(leftList))
    
    ___ binarySearch2  rawList, target
        split = l..(rawList) // 2
        
        left = rawList[:split]
        right = rawList[split:]
        
        __ n.. left a.. n.. right:
            r_ False
        
        __ left a.. left[-1] __ target:
            r_ True
        
        __ right a.. right[0] __ target:
            r_ True
        
        __ l..(left) > 1 a.. left[-1] > target:
            r_ self.binarySearch2(left, target)
        
        __ l..(right) > 1 a.. right[0] < target:
            r_ self.binarySearch2(right, target)
        
        r_ False
        
    ___ searchMatrix  matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        __ n.. any(matrix
            r_ False
        
        column = [i[0] ___ i __ matrix]
        
        column_result = self.binarySearch(column, target)
        __ column_result __ -1:
            r_ False
        
        r_ self.binarySearch2(matrix[column_result], target)
