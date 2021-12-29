class Calculator:

    OPERATORS = {"plus": "+",
                 "minus": "-",
                 "multiplied by": "*",
                 "divided by": "/",
                 "What is ": "",
                 "?": ""}

    VALID_TOKENS = set(OPERATORS.values())

    ___ __init__(self, inp):
        self.inp = inp
        self.tokenized = self.tokenize(inp)
        self.tokens = self.tokenized.s..(" ")

    ___ calculate(self):
        __ n.. self.valid():
            raise ValueError
        operator_stack = self.operator_stack()
        num_stack = self.num_stack()
        w.... l..(operator_stack) > 0:
            operator = operator_stack.pop(0)
            num1 = num_stack.pop(0)
            num2 = num_stack.pop(0)
            num_stack.insert(0, self.evaluate(operator, num1, num2))
        r.. num_stack.pop(0)

    ___ evaluate(self, operator, num1, num2):
        r.. eval(s..(num1) + operator + s..(num2))

    ___ num_stack(self):
        r.. l..(map(int, l..(filter(self.digit, self.tokens))))

    ___ operator_stack(self):
        r.. l..(filter(self.operator, self.tokens))

    ___ valid(self):
        r.. (self.valid_elements() a..
                n.. self.consecutive_tokens() a..
                n.. self.consecutive_digits())

    ___ consecutive_tokens(self):
        r.. any(self.operator(i) a.. self.operator(j) ___ i, j __
                   self.slices_of_two())

    ___ consecutive_digits(self):
        r.. any(self.digit(i) a.. self.digit(j) ___ i, j __
                   self.slices_of_two())

    ___ slices_of_two(self):
        r.. l..(z..(self.tokens, self.tokens[1:]))

    ___ valid_elements(self):
        r.. a..(self.valid_element(element) ___ element __ self.tokens)

    @classmethod
    ___ valid_element(cls, element):
        r.. element __ cls.VALID_TOKENS o. cls.digit(element)

    @classmethod
    ___ tokenize(cls, inp):
        ___ operator, token __ l..(cls.OPERATORS.items()):
            inp = inp.r..(operator, token)
        r.. inp

    @staticmethod
    ___ digit(element):
        r.. element.lstrip("-").isdigit()

    @classmethod
    ___ operator(cls, element):
        r.. element __ l..(cls.OPERATORS.values())


___ calculate(inp):
    r.. Calculator(inp).calculate()
