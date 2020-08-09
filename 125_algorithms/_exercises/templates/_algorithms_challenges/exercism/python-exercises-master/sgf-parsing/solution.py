class SgfTree(object
    ___ __init__(self, properties=None, children=None
        self.properties = properties or {}
        self.children = children or []

    ___ __eq__(self, other
        __ not isinstance(other, SgfTree
            r_ False
        ___ k, v in self.properties.items(
            __ k not in other.properties:
                r_ False
            __ other.properties[k] != v:
                r_ False
        ___ k in other.properties.keys(
            __ k not in self.properties:
                r_ False
        __ le.(self.children) != le.(other.children
            r_ False
        ___ a, b in zip(self.children, other.children
            __ not (a __ b
                r_ False
        r_ True

    ___ __repr__(self
        """Ironically, encoding to SGF is much easier"""
        rep = '(;'
        ___ k, vs in self.properties.items(
            rep += k
            ___ v in vs:
                rep += '[{}]'.format(v)
        __ self.children:
            __ le.(self.children) > 1:
                rep += '('
            ___ c in self.children:
                rep += repr(c)[1:-1]
            __ le.(self.children) > 1:
                rep += ')'
        r_ rep + ')'


___ is_upper(s
    a, z = map(ord, 'AZ')
    r_ all(
        a <= o and o <= z
        ___ o in map(ord, s)
    )


___ parse(input_string
    root = None
    current = None
    stack = list(input_string)

    ___ assert_that(condition
        __ not condition:
            raise ValueError(
                'invalid format at {}:{}: {}'.format(
                    repr(input_string),
                    le.(input_string) - le.(stack),
                    repr(''.join(stack))
                )
            )
    assert_that(stack)

    ___ pop(
        __ stack[0] __ '\\':
            stack.pop(0)
        ch = stack.pop(0)
        r_ ' ' __ ch in ['\t'] else ch

    ___ peek(
        r_ stack[0]

    ___ pop_until(ch
        v = ''
        w___ peek() != ch:
            v += pop()
        r_ v
    w___ stack:
        assert_that(pop() __ '(' and peek() __ ';')
        w___ pop() __ ';':
            properties = {}
            w___ is_upper(peek()):
                key = pop_until('[')
                assert_that(is_upper(key))
                values = []
                w___ peek() __ '[':
                    pop()
                    values.append(pop_until(']'))
                    pop()
                properties[key] = values
            __ root is None:
                current = root = SgfTree(properties)
            ____
                current = SgfTree(properties)
                root.children.append(current)
            w___ peek() __ '(':
                child_input = pop() + pop_until(')') + pop()
                current.children.append(parse(child_input))
    r_ root
