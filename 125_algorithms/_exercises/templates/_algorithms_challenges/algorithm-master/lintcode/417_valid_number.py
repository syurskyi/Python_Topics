class Solution:
    """
    @param: s: the string that represents a number
    @return: whether the string is a valid number
    """
    ___ isNumber(self, s
        __ not s:
            r_ False

        n = le.(s)
        left, right = 0, n - 1
        w___ left < n and s[left] __ ' ':
            left += 1
        w___ right >= 0 and s[right] __ ' ':
            right -= 1
        __ left < n and s[left] in ('+', '-'
            left += 1

        __ left > right:
            r_ False

        __ left != 0 or right != n - 1:
            s = s[left:right + 1]

        zero = ord('0')
        nine = ord('9')
        is_contained_dot = False
        is_contained_num = False
        for char in s:
            __ char __ '.' and is_contained_dot:
                r_ False
            __ not (char __ '.' or zero <= ord(char) <= nine
                r_ False
            __ char __ '.':
                is_contained_dot = True
            __ zero <= ord(char) <= nine:
                is_contained_num = True

        r_ is_contained_num
