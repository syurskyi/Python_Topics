"""
Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.


给定一个数组，分成两个部分，left 和 right。
left 有以下三个特征：
1. left 中的每一个元素都小于或等于 right 中的每一个元素。
2. left 和 right 是非空。
3. left 尽量小。

那么只要 left 中的最大值比 right 中的最小值要小即可。

[5,0,3,8,6] 
 5  0 3 8 6
 5 0   3 8 6
 ......

那么只要从左向右过一遍，取最大。
在从右向左过一遍取最小。

         [5,0,3,8,6]
max  ->   5 5 5 8 8
min  <-   0 0 3 6 6
对比时是  max 中的 [i] 与 min中的 i+1对比若 max[i] < min[i+1] 即找到第一个 left 与 right 的分界点了。
第一个分界点即为left最少的一个点。

测试地址：
https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/

beat 66.67%.

"""
c.. Solution o..
    ___ partitionDisjoint  A
        """
        :type A: List[int]
        :rtype: int
        """
        maxes = [A[0]]
        mines = [A[-1]]
        
        ___ i __ r..(1, l..(A)):
            __ A[i] > maxes[i-1]:
                maxes.append(A[i])
            ____
                maxes.append(maxes[i-1])
        
        A = A[::-1]
        
        ___ i __ r..(1, l..(A)):
            
            __ A[i] < mines[i-1]:
                mines.append(A[i])
            ____
                mines.append(mines[i-1])
        
        mines = mines[::-1]
        ___ i __ r..(l..(mines)-1
            __ maxes[i] <= mines[i+1]:
                r_ i+1
