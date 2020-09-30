import re

___ foo(obj):
    all_attributes = dir(obj)
    normal_attributes = [attribute \
    ___ attribute __ all_attributes \
        if not re.compile("__[a-z0-9A-Z_]*__").search(attribute)]
    r_ normal_attributes

