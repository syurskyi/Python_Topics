______ re

___ foo(obj):
    all_attributes _ dir(obj)
    normal_attributes _ [attribute \
    ___ attribute __ all_attributes \
        __ not re.compile("__[a-z0-9A-Z_]*__").search(attribute)]
    r_ normal_attributes

