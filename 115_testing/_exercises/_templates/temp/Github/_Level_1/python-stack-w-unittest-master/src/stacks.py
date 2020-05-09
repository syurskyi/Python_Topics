c_ Stack(object
    """docstring for Stack"""
    ___  -
        super(Stack, self). - ()
        stack _ []

    ___ is_empty
        r_ stack __ []

    ___ push  data
        stack.append(data)

    ___ pop
        __ is_empty(
            r_ None

        data _ stack[-1]
        del stack[-1]
        r_ data

    ___ peek
        __ is_empty(
            r_ None

        r_ stack[-1]

    ___ size
        r_ len(stack)
