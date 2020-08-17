___ is_empty(stack
    r_ stack __ []


class CheckBrackets:
    BRACKETS = {'{': '}',
                '[': ']',
                '(': ')'}
    OPENING_BRACKET = set(BRACKETS.keys())
    CLOSING_BRACKET = set(BRACKETS.values())

    ___ __init__(self, inp
        self.inp = inp

    ___ is_paired(self
        stack = []
        ___ bracket in self.get_brackets(self.inp
            __ self.is_opening_bracket(bracket
                stack.append(bracket)
            ____ self.is_closing_bracket(bracket) and self.closes_existing_bracket(bracket, stack
                stack.p..
            ____
                r_ False  # This is an invalid closing bracket

        r_ is_empty(stack)  # There are more open brackets left to close

    ___ closes_existing_bracket(self, char, stack
        r_ stack and self.matching_brackets(stack[-1], char)

    ___ matching_brackets(self, opener, closer
        r_ self.BRACKETS[opener] __ closer

    ___ get_brackets(self, string
        r_ [char ___ char in string __ self.is_bracket(char)]

    ___ is_opening_bracket(self, bracket
        r_ bracket in self.OPENING_BRACKET

    ___ is_closing_bracket(self, bracket
        r_ bracket in self.CLOSING_BRACKET

    ___ is_bracket(self, char
        r_ self.is_opening_bracket(char) or self.is_closing_bracket(char)


___ is_paired(inp
    r_ CheckBrackets(inp).is_paired()
