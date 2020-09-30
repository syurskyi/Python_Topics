# Sort Colours
# Question: Given an array with n objects coloured red, white or blue, sort them so that objects of the same colour are adjacent, with the colours in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the colour red, white, and blue respectively.
# Note: You are not supposed to use the library's sort function for this problem
# Solutions:


class Solution:
    # @param A a list of integers
    # @return sorted A, sort in place
    ___ sortColors(self, A):
        color=[0]*3
        ___ i __ A:
            color[i] += 1
        i = 0
        ___ x __ range(3):
            ___ j __ range(color[x]):
                A[i]=x
                i+=1
        r_ A


Solution().sortColors([1,2,0,1,2,0])