c_ SgfTree(object):
    ___ - , properties=N.., children_ N..
        properties = properties o. {}
        children = children o. []

    ___ __eq__(self, other):
        __ n.. isi..(other, SgfTree):
            r.. F..
        ___ k, v __ properties.i..:
            __ k n.. __ other.properties:
                r.. F..
            __ other.properties[k] != v:
                r.. F..
        ___ k __ other.properties.k..:
            __ k n.. __ properties:
                r.. F..
        __ l..(children) != l..(other.children):
            r.. F..
        ___ a, b __ z..(children, other.children):
            __ n.. (a __ b):
                r.. F..
        r.. T..

    ___ __repr__
        """Ironically, encoding to SGF is much easier"""
        rep = '(;'
        ___ k, vs __ properties.i..:
            rep += k
            ___ v __ vs:
                rep += '[{}]'.f..(v)
        __ children:
            __ l..(children) > 1:
                rep += '('
            ___ c __ children:
                rep += repr(c)[1:-1]
            __ l..(children) > 1:
                rep += ')'
        r.. rep + ')'


___ is_upper(s):
    a, z = map(ord, 'AZ')
    r.. a..(
        a <= o a.. o <= z
        ___ o __ map(ord, s)
    )


___ parse(input_string):
    root = N..
    current = N..
    stack = l..(input_string)

    ___ assert_that(condition):
        __ n.. condition:
            raise ValueError(
                'invalid format at {}:{}: {}'.f..(
                    repr(input_string),
                    l..(input_string) - l..(stack),
                    repr(''.j..(stack))
                )
            )
    assert_that(stack)

    ___ pop
        __ stack[0] __ '\\':
            stack.pop(0)
        ch = stack.pop(0)
        r.. ' ' __ ch __ ['\t'] ____ ch

    ___ peek
        r.. stack[0]

    ___ pop_until(ch):
        v = ''
        w.... peek() != ch:
            v += pop()
        r.. v
    w.... stack:
        assert_that(pop() __ '(' a.. peek() __ ';')
        w.... pop() __ ';':
            properties    # dict
            w.... is_upper(peek()):
                key = pop_until('[')
                assert_that(is_upper(key))
                values    # list
                w.... peek() __ '[':
                    pop()
                    values.a..(pop_until(']'))
                    pop()
                properties[key] = values
            __ root __ N..
                current = root = SgfTree(properties)
            ____:
                current = SgfTree(properties)
                root.children.a..(current)
            w.... peek() __ '(':
                child_input = pop() + pop_until(')') + pop()
                current.children.a..(parse(child_input))
    r.. root
