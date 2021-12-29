___ is_empty(stack):
    r.. stack __ []


class CheckBrackets:
    BRACKETS = {'{': '}',
                '[': ']',
                '(': ')'}
    OPENING_BRACKET = set(BRACKETS.keys())
    CLOSING_BRACKET = set(BRACKETS.values())

    ___ __init__(self, inp):
        self.inp = inp

    ___ is_paired(self):
        stack    # list
        ___ bracket __ self.get_brackets(self.inp):
            __ self.is_opening_bracket(bracket):
                stack.a..(bracket)
            ____ self.is_closing_bracket(bracket) and self.closes_existing_bracket(bracket, stack):
                stack.pop()
            ____:
                r.. False  # This is an invalid closing bracket

        r.. is_empty(stack)  # There are more open brackets left to close

    ___ closes_existing_bracket(self, char, stack):
        r.. stack and self.matching_brackets(stack[-1], char)

    ___ matching_brackets(self, opener, closer):
        r.. self.BRACKETS[opener] __ closer

    ___ get_brackets(self, string):
        r.. [char ___ char __ string __ self.is_bracket(char)]

    ___ is_opening_bracket(self, bracket):
        r.. bracket __ self.OPENING_BRACKET

    ___ is_closing_bracket(self, bracket):
        r.. bracket __ self.CLOSING_BRACKET

    ___ is_bracket(self, char):
        r.. self.is_opening_bracket(char) o. self.is_closing_bracket(char)


___ is_paired(inp):
    r.. CheckBrackets(inp).is_paired()
