___ check_brackets(string
    counterparts = {')': '(', '}': '{', ']': '['}

    stack = []
    ___ char in string:
        __ char in counterparts.values(
            stack.append(char)
        ____ char in counterparts:
            __ not stack:
                r_ False
            __ stack.pop() != counterparts[char]:
                r_ False
    r_ not stack
