___ is_empty(stack):
    return stack == []


class CheckBrackets:
    BRACKETS = {'{': '}',
                '[': ']',
                '(': ')'}
    OPENING_BRACKET = set(BRACKETS.keys())
    CLOSING_BRACKET = set(BRACKETS.values())

    ___ __init__(self, inp):
        self.inp = inp

    ___ is_paired(self):
        stack = []
        for bracket in self.get_brackets(self.inp):
            __ self.is_opening_bracket(bracket):
                stack.append(bracket)
            elif self.is_closing_bracket(bracket) and self.closes_existing_bracket(bracket, stack):
                stack.pop()
            else:
                return False  # This is an invalid closing bracket

        return is_empty(stack)  # There are more open brackets left to close

    ___ closes_existing_bracket(self, char, stack):
        return stack and self.matching_brackets(stack[-1], char)

    ___ matching_brackets(self, opener, closer):
        return self.BRACKETS[opener] == closer

    ___ get_brackets(self, string):
        return [char for char in string __ self.is_bracket(char)]

    ___ is_opening_bracket(self, bracket):
        return bracket in self.OPENING_BRACKET

    ___ is_closing_bracket(self, bracket):
        return bracket in self.CLOSING_BRACKET

    ___ is_bracket(self, char):
        return self.is_opening_bracket(char) or self.is_closing_bracket(char)


___ is_paired(inp):
    return CheckBrackets(inp).is_paired()
