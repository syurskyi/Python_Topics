"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

根据单双排列，一个双一个单。

"""
c.. Solution o..
    ___ sortArrayByParityII  A
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        odd   # list
        even   # list
        
        ___ i __ A:
            __ i%2 __ 0:
                even.append(i)
            ____
                odd.append(i)
        
        result   # list
        ___ j, k __ zip(even, odd
            result.append(j)
            result.append(k)
        r_ result
        