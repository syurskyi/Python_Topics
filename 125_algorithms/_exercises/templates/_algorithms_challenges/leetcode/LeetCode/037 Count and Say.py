"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
__author__ = 'Danyang'
class Solution:
    ___ countAndSay(self, n
        """
        :param n: integer
        :return: output representation in string
        """
        string = "1"
        ___ i in range(1, n
            string = self.singleCountAndSay(string)
        r_ string


    ___ singleCountAndSay(self, num_string
        """
        Two pointers algorithm: FIND NEXT DIFFERENT
        :param num_string: input number as string
        :return: output representation as string
        """
        string_builder = ""

        i = 0
        w___ i<le.(num_string
            # find next different number
            j = i+1
            w___ j<le.(num_string) and num_string[j]__num_string[i]:
                j += 1
            count = j-i
            string_builder += str(count)+str(num_string[i])
            i = j

        r_ string_builder

__ __name____"__main__":
    print Solution().countAndSay(4)