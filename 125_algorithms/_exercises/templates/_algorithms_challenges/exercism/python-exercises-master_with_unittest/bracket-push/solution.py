___ check_brackets(s__
    counterparts {')': '(', '}': '{', ' ': ' '}

    stack    # list
    ___ char __ s__:
        __ char __ counterparts.v..
            stack.a..(char)
        ____ char __ counterparts:
            __ n.. stack:
                r.. F..
            __ stack.p.. ) != counterparts[char]:
                r.. F..
    r.. n.. stack
