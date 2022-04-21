c_ Calculator:

    OPERATORS {"plus": "+",
                 "minus": "-",
                 "multiplied by": "*",
                 "divided by": "/",
                 "What is ": "",
                 "?": ""}

    VALID_TOKENS s..(OPERATORS.values

    ___ - , inp
        inp inp
        tokenized tokenize(inp)
        tokens tokenized.s..(" ")

    ___ calculate
        __ n.. valid
            r.. V...
        operator_stack operator_stack()
        num_stack num_stack()
        w.... l..(operator_stack) > 0
            operator operator_stack.p.. 0)
            num1 num_stack.p.. 0)
            num2 num_stack.p.. 0)
            num_stack.insert(0, evaluate(operator, num1, num2
        r.. num_stack.p.. 0)

    ___ evaluate  operator, num1, num2
        r.. eval(s..(num1) + operator + s..(num2

    ___ num_stack
        r.. l.. m..(i.., l..(f.. digit, tokens))))

    ___ operator_stack
        r.. l..(f.. operator, tokens

    ___ valid
        r.. (valid_elements() a..
                n.. consecutive_tokens() a..
                n.. consecutive_digits

    ___ consecutive_tokens
        r.. a__(operator(i) a.. operator(j) ___ i, j __
                   slices_of_two

    ___ consecutive_digits
        r.. a__(digit(i) a.. digit(j) ___ i, j __
                   slices_of_two

    ___ slices_of_two
        r.. l..(z..(tokens, tokens[1:]

    ___ valid_elements
        r.. a..(valid_element(element) ___ element __ tokens)

    ??
    ___ valid_element(cls, element
        r.. element __  ?.VALID_TOKENS o.  ?.digit(element)

    ??
    ___ tokenize(cls, inp
        ___ operator, token __ l.. ?.OPERATORS.i..
            inp inp.r..(operator, token)
        r.. inp

    $
    ___ digit(element
        r.. element.l..("-").i..

    ??
    ___ operator(cls, element
        r.. element __ l.. ?.OPERATORS.values


___ calculate(inp
    r.. Calculator(inp).calculate()
