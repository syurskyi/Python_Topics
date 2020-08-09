class StackUnderflowError(Exception
    pass


keywords = {
    '+': (2, lambda a, b: (a + b,)),
    '-': (2, lambda a, b: (a - b,)),
    '*': (2, lambda a, b: (a * b,)),
    '/': (2, lambda a, b: (a // b,)),
    'swap': (2, lambda a, b: (b, a)),
    'over': (2, lambda a, b: (a, b, a)),
    'dup': (1, lambda x: (x, x)),
    'drop': (1, lambda x: tuple()),
    }


___ evaluate(input_data
    tokens = [token ___ line in input_data ___ token in line.split()]
    stack = []
    env = {}
    w___ tokens:
        token = tokens.pop(0).lower()
        __ token __ ':':
            keyword = tokens.pop(0).lower()
            __ keyword.isdigit(
                raise ValueError("Variables cannot be numbers: " + keyword)
            env[keyword] = [tokens.pop(0)]
            w___ env[keyword][-1] != ';':
                env[keyword].append(tokens.pop(0))
            env[keyword].pop()
        ____ token in env:
            tokens.extend(env[token])
        ____ token in keywords:
            try:
                n_args, func = keywords[token]
                args = tuple(reversed([stack.pop() ___ _ in range(n_args)]))
                stack.extend(func(*args))
            except IndexError:
                raise StackUnderflowError('Cannot apply ' + token)
        ____
            stack.append(int(token))
    r_ stack
