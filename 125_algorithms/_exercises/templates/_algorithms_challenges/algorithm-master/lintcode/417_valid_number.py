c_ Solution:
    """
    @param: s: the string that represents a number
    @return: whether the string is a valid number
    """
    ___ isNumber(self, s):
        __ n.. s:
            r.. F..

        n = l..(s)
        left, right = 0, n - 1
        w.... left < n a.. s[left] __ ' ':
            left += 1
        w.... right >= 0 a.. s[right] __ ' ':
            right -= 1
        __ left < n a.. s[left] __ ('+', '-'):
            left += 1

        __ left > right:
            r.. F..

        __ left != 0 o. right != n - 1:
            s = s[left:right + 1]

        zero = ord('0')
        nine = ord('9')
        is_contained_dot = F..
        is_contained_num = F..
        ___ char __ s:
            __ char __ '.' a.. is_contained_dot:
                r.. F..
            __ n.. (char __ '.' o. zero <= ord(char) <= nine):
                r.. F..
            __ char __ '.':
                is_contained_dot = T..
            __ zero <= ord(char) <= nine:
                is_contained_num = T..

        r.. is_contained_num
