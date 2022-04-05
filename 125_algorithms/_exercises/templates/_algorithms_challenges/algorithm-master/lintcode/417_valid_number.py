c_ Solution:
    """
    @param: s: the string that represents a number
    @return: whether the string is a valid number
    """
    ___ isNumber  s
        __ n.. s:
            r.. F..

        n = l..(s)
        left, right = 0, n - 1
        w.... left < n a.. s[left] __ ' ':
            left += 1
        w.... right >_ 0 a.. s[right] __ ' ':
            right -_ 1
        __ left < n a.. s[left] __ ('+', '-'
            left += 1

        __ left > right:
            r.. F..

        __ left != 0 o. right != n - 1:
            s = s[left:right + 1]

        zero = o..('0')
        nine = o..('9')
        is_contained_dot = F..
        is_contained_num = F..
        ___ char __ s:
            __ char __ '.' a.. is_contained_dot:
                r.. F..
            __ n.. (char __ '.' o. zero <_ o..(char) <_ nine
                r.. F..
            __ char __ '.':
                is_contained_dot = T..
            __ zero <_ o..(char) <_ nine:
                is_contained_num = T..

        r.. is_contained_num
