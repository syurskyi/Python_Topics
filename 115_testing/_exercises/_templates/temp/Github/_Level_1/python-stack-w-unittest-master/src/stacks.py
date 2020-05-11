c_ Stack o..
    """docstring for Stack"""
    ___  -
        super(Stack, self). - ()
        stack _ # list

    ___ is_empty
        r_ stack __ # list

    ___ push  data
        stack.a..(data)

    ___ pop
        __ is_empty(
            r_ N..

        data _ stack[-1]
        del stack[-1]
        r_ data

    ___ peek
        __ is_empty(
            r_ N..

        r_ stack[-1]

    ___ size
        r_ le.(stack)
