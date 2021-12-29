class Solution:
    """
    @param: s: the string that represents a number
    @return: whether the string is a valid number
    """
    ___ isNumber(self, s):
        __ not s:
            return False

        n = len(s)
        left, right = 0, n - 1
        while left < n and s[left] == ' ':
            left += 1
        while right >= 0 and s[right] == ' ':
            right -= 1
        __ left < n and s[left] in ('+', '-'):
            left += 1

        __ left > right:
            return False

        __ left != 0 or right != n - 1:
            s = s[left:right + 1]

        zero = ord('0')
        nine = ord('9')
        is_contained_dot = False
        is_contained_num = False
        for char in s:
            __ char == '.' and is_contained_dot:
                return False
            __ not (char == '.' or zero <= ord(char) <= nine):
                return False
            __ char == '.':
                is_contained_dot = True
            __ zero <= ord(char) <= nine:
                is_contained_num = True

        return is_contained_num
