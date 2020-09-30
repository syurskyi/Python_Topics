# Multiply Strings
# Question: Given two numbers represented as strings, return multiplication of the numbers as a string.
# Note: The numbers can be arbitrarily large and are non-negative
# Solutions:

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))


Solution().multiply("122326161616161616","-161651616161616")