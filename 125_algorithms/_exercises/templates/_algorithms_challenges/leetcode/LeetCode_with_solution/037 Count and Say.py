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
c_ Solution:
    ___ countAndSay(self, n):
        """
        :param n: integer
        :return: output representation in string
        """
        s__ = "1"
        ___ i __ r..(1, n):
            s__ = singleCountAndSay(s__)
        r.. s__


    ___ singleCountAndSay(self, num_string):
        """
        Two pointers algorithm: FIND NEXT DIFFERENT
        :param num_string: input number as string
        :return: output representation as string
        """
        string_builder = ""

        i = 0
        w.... i<l..(num_string):
            # find next different number
            j = i+1
            w.... j<l..(num_string) a.. num_string[j]__num_string[i]:
                j += 1
            count = j-i
            string_builder += s..(count)+s..(num_string[i])
            i = j

        r.. string_builder

__ __name____"__main__":
    print Solution().countAndSay(4)