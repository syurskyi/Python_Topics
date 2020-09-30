# Count and Say
# Question: The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# Note: The sequence of integers will be represented as a string.
# Solutions:


class Solution:
    # @return a string
    def countAndSay(n):
        result = "1"
        if n == 0:
            return None
        else:
            print ( "1" )
            for i in range(n-1):
                temp = ""
                current = result[0]
                currentCount = 1
                for item in result[1:]:
                    if item == current:
                        currentCount += 1
                    else:
                        temp += str(currentCount) + current
                        current = item
                        currentCount = 1
                temp += str(currentCount) + current
                result = temp
                print(result)

Solution.countAndSay(8)