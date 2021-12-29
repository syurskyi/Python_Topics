___ check_brackets(string):
    counterparts = {')': '(', '}': '{', ']': '['}

    stack    # list
    ___ char __ string:
        __ char __ counterparts.values():
            stack.a..(char)
        ____ char __ counterparts:
            __ n.. stack:
                r.. False
            __ stack.pop() != counterparts[char]:
                r.. False
    r.. n.. stack
