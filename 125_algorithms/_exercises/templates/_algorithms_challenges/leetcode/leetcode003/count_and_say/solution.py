"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


c_ Solution(o..
    ___ countAndSay  n
        """
        :type n: int
        :rtype: str
        """
        ln l..(s..(1
        ___ i __ r..(1, n
            tn    # list
            count 1
            prev N..
            ___ c __ ln:
                __ prev __ c:
                    count += 1
                __ prev __ n.. N.. a.. prev !_ c:
                    tn.a..(s..(count
                    tn.a..(s..(prev
                    count 1
                prev c
            tn.a..(s..(count
            tn.a..(s..(prev
            ln tn
        r.. ''.j..(ln)


s Solution()
print s.countAndSay(1)
print s.countAndSay(2)
print s.countAndSay(3)
print s.countAndSay(4)
print s.countAndSay(5)
