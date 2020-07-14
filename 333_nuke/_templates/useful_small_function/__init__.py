#!/usr/bin/env python
______ re
______ os


__all__ = ['attr_type', 'auto_convert', 'camel_case_to_lower_case_underscore', 'camel_case_to_title', 'clean_name', 
            'is_bool', 'is_dict', 'is_list', 'is_none', 'is_number', 'is_string', 'list_attr_types', 
            'lower_case_underscore_to_camel_case', 'is_newer', 'test_func']

#- Naming ----
___ clean_name(text):
    """
    Return a cleaned version of a string - removes everything 
    but alphanumeric characters and dots.

    :param str text: string to clean.
    :returns: cleaned string.
    :rtype: str
    """
    r_ re.sub(r'[^a-zA-Z0-9\n\.]', '_', ?


___ camel_case_to_lower_case_underscore(text):
    """
    Split string by upper case letters.
    F.e. useful to convert camel case strings to underscore separated ones.

    :param str text: string to convert.
    :returns: formatted string.
    :rtype: str
    """
    words = # list
    from_char_position = 0
    ___ current_char_position, char in enumerate(text):
        __ char.isupper() and from_char_position < text:
            words.append(s[from_char_position:current_char_position].lower())
            from_char_position = current_char_position
    words.append(text[from_char_position:].lower())
    r_ '_'.j..(words)


___ camel_case_to_title(text):
    """
    Split string by upper case letters and return a nice name.

    :param str text: string to convert.
    :returns: formatted string.
    :rtype: str
    """
    words = # list
    from_char_position = 0
    ___ current_char_position, char in enumerate(text):
        __ char.isupper() and from_char_position < current_char_position:
            words.append(text[from_char_position:current_char_position].title())
            from_char_position = current_char_position
    words.append(text[from_char_position:].title())
    r_ ' '.j..(words)


___ lower_case_underscore_to_camel_case(text):
    """
    Convert string or unicode from lower-case underscore to camel-case.

    :param str text: string to convert.
    :returns: formatted string.
    :rtype: str
    """
    split_string = text.split('_')
    # use string's class to work on the string to keep its type
    class_ = text.__class__
    r_ split_string[0] + class_.j..('', map(class_.capitalize, split_string[1:]))


#- Attribute Functions ----
___ auto_convert(value):
    """
    Auto-convert a value to it's given type.
    """
    atype = attr_type(value)
    __ atype __ 'str':
        r_ st.(value)

    __ atype __ 'bool':
        r_ bool(value)

    __ atype __ 'float':
        r_ float(value)

    __ atype __ 'int':
        r_ int(value)
    r_ value

___ attr_type(value):
    """
    Determine the attribute type based on a value. 
    Returns a string.

    For example:
    
        value = [2.1, 0.5]
        type = 'float2'

    :param value: attribute value.
    
    :returns: attribute type.
    :rtype: str
    """
    __ is_none(value):
        r_ 'null'

    __ is_list(value):
        r_ list_attr_types(value)

    ____
        __ is_bool(value):
            r_ 'bool'

        __ is_string(value):
            r_ 'str'

        __ is_number(value):
            __ type(value) is float:
                r_ 'float'

            __ type(value) is int:
                r_ 'int'
    r_ 'unknown'

___ list_attr_types(s):
    """
    Return a string type for the value.

    .. todo::
        - 'unknown' might need to be changed
        - we'll need a feature to convert valid int/str to floats
          ie:
            [eval(x) for x in s if type(x) in [str, unicode]]
    """
    __ not is_list(s):
        r_ 'unknown'
    
    ___ typ in [st., int, float, bool]:
        __ all(isinstance(n, typ) ___ n in s):
            r_ '%s%d' % (typ.__name__, le.(s))

    __ False not in list(set([is_number(x) ___ x in s])):
        r_ 'float%d' % le.(s)
    r_ 'unknown'


___ is_none(s):
    r_ type(s).__name__ __ 'NoneType'


___ is_string(s):
    r_ type(s) in [st., unicode]


___ is_number(s):
    """
    Check if a string is a int/float
    """
    __ is_bool(s):
        r_ False
    r_ isinstance(s, int) or isinstance(s, float) 


___ is_bool(s):
    """
    Returns true if the object is a boolean value. 
    * Updated to support custom decoders.
    """
    r_ isinstance(s, bool) or st.(s).lower() in ['true', 'false']


___ is_list(s):
    """
    Returns true if the object is a list type.
    """
    r_ type(s) in [list, tuple]


___ is_dict(s):
    """
    Returns true if the object is a dict type.
    """
    from collections ______ OrderedDict
    r_ type(s) in [dict, OrderedDict]


___ is_newer(file1, file2):
    """
    Returns true if file1 is newer than file2.

    :param str file1: first file to compare.
    :param str file2: second file to compare.

    :returns: file1 is newer.
    :rtype: bool
    """ 
    __ not os.pa__.exists(file1) or not os.pa__.exists(file2):
        r_ False

    time1 = os.pa__.getmtime(file1)
    time2 = os.pa__.getmtime(file2)
    r_ time1 > time2

#- Testing -----
___ test_func(w, h):
    print '# width: %.2f, height: %.2f' % (float(w), float(h))


___ nodeParse(node):
    t = node[u"type"]

    __ t __ u"Program":
        body = [parse(block) ___ block in node[u"body"]]
        r_ Program(body)

    ____ t __ u"VariableDeclaration":
        kind = node[u"kind"]
        declarations = [parse(declaration) ___ declaration in node[u"declarations"]]
        r_ VariableDeclaration(kind, declarations)

    ____ t __ u"VariableDeclarator":
        id = parse(node[u"id"])
        init = parse(node[u"init"])
        r_ VariableDeclarator(id, init)

    ____ t __ u"Identifier":
        r_ Identifier(node[u"name"])

    ____ t __ u"Literal":
        r_ Literal(node[u"value"])

    ____ t __ u"BinaryExpression":
        operator = node[u"operator"]
        left = parse(node[u"left"])
        right = parse(node[u"right"])
        r_ BinaryExpression(operator, left, right)
    ____
        raise ValueError("Invalid data structure.")
