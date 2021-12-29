___ check_brackets(string):
    counterparts = {')': '(', '}': '{', ']': '['}

    stack = []
    for char in string:
        __ char in counterparts.values():
            stack.append(char)
        elif char in counterparts:
            __ not stack:
                return False
            __ stack.pop() != counterparts[char]:
                return False
    return not stack
