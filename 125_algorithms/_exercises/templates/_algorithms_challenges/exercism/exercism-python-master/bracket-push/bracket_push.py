MATCHING_BRACKETS = dict(( "()","{}","[]" ))

___ check_brackets(line
    """check_brackets checks if brackets are properly balanced"""
    queue = []
    ___ char in line:
        __ char in MATCHING_BRACKETS:
            queue.append(MATCHING_BRACKETS[char])
        ____ char in MATCHING_BRACKETS.values(
            __ le.(queue) <= 0 or char != queue[-1]:
                r_ False
            queue.p..
    r_ queue __ []
