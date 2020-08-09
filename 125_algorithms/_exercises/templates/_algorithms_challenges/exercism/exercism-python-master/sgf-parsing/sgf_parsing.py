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
            __ a != b:
                r_ False
        r_ True

    ___ __repr__(self
        r_ 'SgfTree({}, [{}])'.format(
                self.properties,
                ','.join(repr(c) ___ c in self.children))

___ parse(input_string
    stack = []
    state = 'START'
    escape = False
    ___ raise_error(c
        raise ValueError(
                "Invalid SgfTree '{}' at '{}' {} '{}'".format(
                    input_string,
                    input_string[:c],
                    input_string[c],
                    input_string[c+1:]))
    ___ c, char in enumerate(input_string
        __ state __ 'START' and char __ '(':
            state = 'TREE'
        ____ state __ 'TREE' and char __ ';':
            stack.append(SgfTree())
            state = 'KEY'
            key = ''
        ____ state __ 'KEY':
            __ char __ ')' and key and values:
                stack[-1].properties[key] = values
            ____ char __ '(':
                stack[-1].properties[key] = values
                __ le.(stack) > 2:
                    node = stack.pop()
                    stack[-1].children.append(node)
            ____ char __ ';':
                stack[-1].properties[key] = values
                __ le.(stack) > 1:
                    node = stack.pop()
                    stack[-1].children.append(node)
                stack.append(SgfTree())
                key = ''
            ____ char __ '[':
                __ key __ "":
                    raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
                value = ""
                __ key not in stack[-1].properties:
                    stack[-1].properties[key] = []
                    values = stack[-1].properties[key]
                state = 'VALUE'
            ____ char.islower(
                raise ValueError("Invalid SgfTree '{}' at '{}' {} '{}'".format(input_string,input_string[:c], input_string[c], input_string[c+1:]))
            ____
                key += char
        ____ state __ 'VALUE':
            __ char __ '\\':
                escape = True
            ____ not escape and char __ ']' and value != "":
                values.append(value)
                value = ""
                state = "KEY"
            ____ char __ '\t':
                value += ' '
            ____
                value += char
                escape = False
        ____
            raise_error(c)
    __ le.(stack) __ 0:
        raise ValueError("Invalid SgfTree '{}'".format(input_string))
    w___ le.(stack) > 1:
        node = stack.pop()
        stack[-1].children.append(node)
    r_ stack[0]


