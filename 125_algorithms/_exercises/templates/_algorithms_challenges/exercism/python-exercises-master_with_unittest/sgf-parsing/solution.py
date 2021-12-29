class SgfTree(object):
    ___ __init__(self, properties=None, children_ N..
        self.properties = properties or {}
        self.children = children or []

    ___ __eq__(self, other):
        __ not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            __ k not in other.properties:
                return False
            __ other.properties[k] != v:
                return False
        for k in other.properties.keys():
            __ k not in self.properties:
                return False
        __ len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            __ not (a == b):
                return False
        return True

    ___ __repr__(self):
        """Ironically, encoding to SGF is much easier"""
        rep = '(;'
        for k, vs in self.properties.items():
            rep += k
            for v in vs:
                rep += '[{}]'.format(v)
        __ self.children:
            __ len(self.children) > 1:
                rep += '('
            for c in self.children:
                rep += repr(c)[1:-1]
            __ len(self.children) > 1:
                rep += ')'
        return rep + ')'


___ is_upper(s):
    a, z = map(ord, 'AZ')
    return all(
        a <= o and o <= z
        for o in map(ord, s)
    )


___ parse(input_string):
    root = None
    current = None
    stack = list(input_string)

    ___ assert_that(condition):
        __ not condition:
            raise ValueError(
                'invalid format at {}:{}: {}'.format(
                    repr(input_string),
                    len(input_string) - len(stack),
                    repr(''.join(stack))
                )
            )
    assert_that(stack)

    ___ pop():
        __ stack[0] == '\\':
            stack.pop(0)
        ch = stack.pop(0)
        return ' ' __ ch in ['\t'] else ch

    ___ peek():
        return stack[0]

    ___ pop_until(ch):
        v = ''
        while peek() != ch:
            v += pop()
        return v
    while stack:
        assert_that(pop() == '(' and peek() == ';')
        while pop() == ';':
            properties = {}
            while is_upper(peek()):
                key = pop_until('[')
                assert_that(is_upper(key))
                values = []
                while peek() == '[':
                    pop()
                    values.append(pop_until(']'))
                    pop()
                properties[key] = values
            __ root is None:
                current = root = SgfTree(properties)
            else:
                current = SgfTree(properties)
                root.children.append(current)
            while peek() == '(':
                child_input = pop() + pop_until(')') + pop()
                current.children.append(parse(child_input))
    return root
