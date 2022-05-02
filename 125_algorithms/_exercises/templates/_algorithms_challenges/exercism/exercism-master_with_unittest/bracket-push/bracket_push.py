___ is_empty(stack
    r.. stack __    # list


c_ CheckBrackets:
    BRACKETS {'{': '}',
                ' ': ' ',
                '(': ')'}
    OPENING_BRACKET s..(BRACKETS.keys
    CLOSING_BRACKET s..(BRACKETS.values

    ___ - , inp
        inp inp

    ___ is_paired
        stack    # list
        ___ bracket __ get_brackets(inp
            __ is_opening_bracket(bracket
                stack.a..(bracket)
            ____ is_closing_bracket(bracket) a.. closes_existing_bracket(bracket, stack
                stack.p.. )
            ____
                r.. F..  # This is an invalid closing bracket

        r.. is_empty(stack)  # There are more open brackets left to close

    ___ closes_existing_bracket  char, stack
        r.. stack a.. matching_brackets(stack[-1], char)

    ___ matching_brackets  opener, closer
        r.. BRACKETS[opener] __ closer

    ___ get_brackets  s__
        r.. [char ___ char __ s__ __ is_bracket(char)]

    ___ is_opening_bracket  bracket
        r.. bracket __ OPENING_BRACKET

    ___ is_closing_bracket  bracket
        r.. bracket __ CLOSING_BRACKET

    ___ is_bracket  char
        r.. is_opening_bracket(char) o. is_closing_bracket(char)


___ is_paired(inp
    r.. CheckBrackets(inp).is_paired()
