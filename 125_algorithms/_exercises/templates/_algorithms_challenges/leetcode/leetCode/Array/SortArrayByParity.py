"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000


开胃菜，偶数放一堆，奇数放一堆。
O(n).

测试链接：
https://leetcode.com/contest/weekly-contest-102/problems/sort-array-by-parity/

contest.

"""
c.. Solution o..
    ___ sortArrayByParity  A
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even   # list
        odd   # list
        ___ i __ A:
            __ i % 2 __ 0:
                even.a.. i)
            ____
                odd.a.. i)
        
        r_ even + odd


                    

