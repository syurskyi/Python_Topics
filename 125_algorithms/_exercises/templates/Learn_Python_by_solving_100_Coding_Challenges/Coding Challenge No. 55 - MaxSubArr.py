# Maximum Subarray
# Question: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# Solutions:


c_ Solution:
    # @param A, a list of integers
    # @return an integer
    ___ maxSubArray(self, A):
        __ le.(A)__0:
            r_ 0
        temp _ 0
        maxSum _ A[0]
        ___ i __ ra..(0, le.(A)):
            temp _ ma.(A[i], A[i]+temp)
            __ temp> maxSum:
                maxSum _ temp
        r_ maxSum


Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])