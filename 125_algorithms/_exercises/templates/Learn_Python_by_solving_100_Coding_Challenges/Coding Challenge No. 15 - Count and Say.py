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
    ___ countAndSay(n):
        result _ "1"
        __ n __ 0:
            r_ None
        ____
            print ( "1" )
            ___ i __ ra..(n-1):
                temp _ ""
                current _ result[0]
                currentCount _ 1
                ___ item __ result[1:]:
                    __ item __ current:
                        currentCount +_ 1
                    ____
                        temp +_ st.(currentCount) + current
                        current _ item
                        currentCount _ 1
                temp +_ st.(currentCount) + current
                result _ temp
                print(result)

Solution.countAndSay(8)