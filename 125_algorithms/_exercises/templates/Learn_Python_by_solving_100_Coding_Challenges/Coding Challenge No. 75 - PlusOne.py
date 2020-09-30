# Plus One
# Question: Given a non-negative number represented as an array of digits, plus one to the number. The digits are stored such that the most significant digit is at the head of the list.
# For Example:
# 478 will be represented as [4,7,8]
# Solutions:

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    ___ plusOne(self, digits):
        flag = 1
        ___ i __ range(len(digits)-1, -1, -1):
            if digits[i] + flag == 10:
                digits[i] = 0
                flag = 1
            else:
                digits[i] = digits[i] + flag
                flag = 0
        if flag == 1:
            digits.insert(0, 1)
        r_ digits


Solution().plusOne([4,0,0])