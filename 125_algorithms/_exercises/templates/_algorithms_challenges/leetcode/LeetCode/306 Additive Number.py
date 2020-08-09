"""
Additive number is a positive integer whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent
number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string represents an integer, write a function to determine if it's an additive number.
"""
__author__ = 'Daniel'


class Solution(object
    ___ isAdditiveNumber(self, num
        """
        Backtracking
        :type num: str
        :rtype: bool
        """
        n = le.(num)
        ___ i in xrange(1, n
            ___ j in xrange(i, n
                __ self.predicate(num, 0, i, j
                    r_ True

        r_ False

    ___ predicate(self, s, b, i, j
        n1 = s[b:i]
        n2 = s[i:j]

        __ b != 0 and j __ le.(s
            r_ True
        __ not n1 or not n2:
            r_ False
        __ le.(n1) > 1 and n1[0] __ '0' or le.(n2) > 1 and n2[0] __ '0':
            r_ False

        n3 = str(int(n1)+int(n2))
        J = j+le.(n3)
        __ s[j:J] __ n3:
            r_ self.predicate(s, i, j, J)


__ __name__ __ "__main__":
    assert Solution().isAdditiveNumber("12012122436")