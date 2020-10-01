# Plus One
# Question: Given a non-negative number represented as an array of digits, plus one to the number. The digits are stored such that the most significant digit is at the head of the list.
# For Example:
# 478 will be represented as [4,7,8]
# Solutions:

c_ Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    ___ plusOne(, digits):
        flag _ 1
        ___ i __ ra..(le.(digits)-1, -1, -1):
            __ digits[i] + flag __ 10:
                digits[i] _ 0
                flag _ 1
            ____
                digits[i] _ digits[i] + flag
                flag _ 0
        __ flag __ 1:
            digits.insert(0, 1)
        r_ digits


Solution().plusOne([4,0,0])