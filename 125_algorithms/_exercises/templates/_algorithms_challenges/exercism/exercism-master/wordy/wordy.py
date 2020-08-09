class Calculator:

    OPERATORS = {"plus": "+",
                 "minus": "-",
                 "multiplied by": "*",
                 "divided by": "/",
                 "What is ": "",
                 "?": ""}

    VALID_TOKENS = set(OPERATORS.values())

    ___ __init__(self, inp
        self.inp = inp
        self.tokenized = self.tokenize(inp)
        self.tokens = self.tokenized.split(" ")

    ___ calculate(self
        __ not self.valid(
            raise ValueError
        operator_stack = self.operator_stack()
        num_stack = self.num_stack()
        w___ le.(operator_stack) > 0:
            operator = operator_stack.pop(0)
            num1 = num_stack.pop(0)
            num2 = num_stack.pop(0)
            num_stack.insert(0, self.evaluate(operator, num1, num2))
        r_ num_stack.pop(0)

    ___ evaluate(self, operator, num1, num2
        r_ eval(str(num1) + operator + str(num2))

    ___ num_stack(self
        r_ list(map(int, list(filter(self.digit, self.tokens))))

    ___ operator_stack(self
        r_ list(filter(self.operator, self.tokens))

    ___ valid(self
        r_ (self.valid_elements() and
                not self.consecutive_tokens() and
                not self.consecutive_digits())

    ___ consecutive_tokens(self
        r_ any(self.operator(i) and self.operator(j) ___ i, j in
                   self.slices_of_two())

    ___ consecutive_digits(self
        r_ any(self.digit(i) and self.digit(j) ___ i, j in
                   self.slices_of_two())

    ___ slices_of_two(self
        r_ list(zip(self.tokens, self.tokens[1:]))

    ___ valid_elements(self
        r_ all(self.valid_element(element) ___ element in self.tokens)

    @classmethod
    ___ valid_element(cls, element
        r_ element in cls.VALID_TOKENS or cls.digit(element)

    @classmethod
    ___ tokenize(cls, inp
        ___ operator, token in list(cls.OPERATORS.items()):
            inp = inp.replace(operator, token)
        r_ inp

    @staticmethod
    ___ digit(element
        r_ element.lstrip("-").isdigit()

    @classmethod
    ___ operator(cls, element
        r_ element in list(cls.OPERATORS.values())


___ calculate(inp
    r_ Calculator(inp).calculate()
