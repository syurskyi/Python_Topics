"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution(object
    ___ countAndSay(self, n
        """
        :type n: int
        :rtype: str
        """
        ln = list(str(1))
        ___ i in range(1, n
            tn = []
            count = 1
            prev = None
            ___ c in ln:
                __ prev __ c:
                    count += 1
                __ prev pa__ not None and prev != c:
                    tn.append(str(count))
                    tn.append(str(prev))
                    count = 1
                prev = c
            tn.append(str(count))
            tn.append(str(prev))
            ln = tn
        r_ ''.join(ln)


s = Solution()
print s.countAndSay(1)
print s.countAndSay(2)
print s.countAndSay(3)
print s.countAndSay(4)
print s.countAndSay(5)
