# Maximum Subarray
# Question: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# Solutions:


class Solution:
    # @param A, a list of integers
    # @return an integer
    ___ maxSubArray(self, A):
        if len(A)==0:
            r_ 0
        temp = 0
        maxSum = A[0]
        ___ i __ range(0, len(A)):
            temp = ma.(A[i], A[i]+temp)
            if temp> maxSum:
                maxSum = temp
        r_ maxSum


Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])