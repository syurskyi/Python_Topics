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
        self.tokens = self.tokenized.split(" ")

    ___ calculate(self):
        __ not self.valid():
            raise ValueError
        operator_stack = self.operator_stack()
        num_stack = self.num_stack()
        while len(operator_stack) > 0:
            operator = operator_stack.pop(0)
            num1 = num_stack.pop(0)
            num2 = num_stack.pop(0)
            num_stack.insert(0, self.evaluate(operator, num1, num2))
        return num_stack.pop(0)

    ___ evaluate(self, operator, num1, num2):
        return eval(str(num1) + operator + str(num2))

    ___ num_stack(self):
        return list(map(int, list(filter(self.digit, self.tokens))))

    ___ operator_stack(self):
        return list(filter(self.operator, self.tokens))

    ___ valid(self):
        return (self.valid_elements() and
                not self.consecutive_tokens() and
                not self.consecutive_digits())

    ___ consecutive_tokens(self):
        return any(self.operator(i) and self.operator(j) for i, j in
                   self.slices_of_two())

    ___ consecutive_digits(self):
        return any(self.digit(i) and self.digit(j) for i, j in
                   self.slices_of_two())

    ___ slices_of_two(self):
        return list(zip(self.tokens, self.tokens[1:]))

    ___ valid_elements(self):
        return all(self.valid_element(element) for element in self.tokens)

    @classmethod
    ___ valid_element(cls, element):
        return element in cls.VALID_TOKENS or cls.digit(element)

    @classmethod
    ___ tokenize(cls, inp):
        for operator, token in list(cls.OPERATORS.items()):
            inp = inp.replace(operator, token)
        return inp

    @staticmethod
    ___ digit(element):
        return element.lstrip("-").isdigit()

    @classmethod
    ___ operator(cls, element):
        return element in list(cls.OPERATORS.values())


___ calculate(inp):
    return Calculator(inp).calculate()
