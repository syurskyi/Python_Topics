___ check_brackets(string):
    counterparts = {')': '(', '}': '{', ']': '['}

    stack    # list
    ___ char __ string:
        __ char __ counterparts.v..
            stack.a..(char)
        ____ char __ counterparts:
            __ n.. stack:
                r.. F..
            __ stack.pop() != counterparts[char]:
                r.. F..
    r.. n.. stack
