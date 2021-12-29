class SgfTree(object):
    ___ __init__(self, properties=N.., children_ N..
        self.properties = properties o. {}
        self.children = children o. []

    ___ __eq__(self, other):
        __ n.. isi..(other, SgfTree):
            r.. False
        ___ k, v __ self.properties.items():
            __ k n.. __ other.properties:
                r.. False
            __ other.properties[k] != v:
                r.. False
        ___ k __ other.properties.keys():
            __ k n.. __ self.properties:
                r.. False
        __ l..(self.children) != l..(other.children):
            r.. False
        ___ a, b __ zip(self.children, other.children):
            __ n.. (a __ b):
                r.. False
        r.. True

    ___ __repr__(self):
        """Ironically, encoding to SGF is much easier"""
        rep = '(;'
        ___ k, vs __ self.properties.items():
            rep += k
            ___ v __ vs:
                rep += '[{}]'.format(v)
        __ self.children:
            __ l..(self.children) > 1:
                rep += '('
            ___ c __ self.children:
                rep += repr(c)[1:-1]
            __ l..(self.children) > 1:
                rep += ')'
        r.. rep + ')'


___ is_upper(s):
    a, z = map(ord, 'AZ')
    r.. a..(
        a <= o and o <= z
        ___ o __ map(ord, s)
    )


___ parse(input_string):
    root = N..
    current = N..
    stack = l..(input_string)

    ___ assert_that(condition):
        __ n.. condition:
            raise ValueError(
                'invalid format at {}:{}: {}'.format(
                    repr(input_string),
                    l..(input_string) - l..(stack),
                    repr(''.join(stack))
                )
            )
    assert_that(stack)

    ___ pop():
        __ stack[0] __ '\\':
            stack.pop(0)
        ch = stack.pop(0)
        r.. ' ' __ ch __ ['\t'] ____ ch

    ___ peek():
        r.. stack[0]

    ___ pop_until(ch):
        v = ''
        while peek() != ch:
            v += pop()
        r.. v
    while stack:
        assert_that(pop() __ '(' and peek() __ ';')
        while pop() __ ';':
            properties = {}
            while is_upper(peek()):
                key = pop_until('[')
                assert_that(is_upper(key))
                values    # list
                while peek() __ '[':
                    pop()
                    values.a..(pop_until(']'))
                    pop()
                properties[key] = values
            __ root __ N..
                current = root = SgfTree(properties)
            ____:
                current = SgfTree(properties)
                root.children.a..(current)
            while peek() __ '(':
                child_input = pop() + pop_until(')') + pop()
                current.children.a..(parse(child_input))
    r.. root
