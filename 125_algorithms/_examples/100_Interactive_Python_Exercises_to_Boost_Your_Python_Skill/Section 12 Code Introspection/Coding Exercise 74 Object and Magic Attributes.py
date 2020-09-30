import re

def foo(obj):
    all_attributes = dir(obj)
    normal_attributes = [attribute \
    for attribute in all_attributes \
        if not re.compile("__[a-z0-9A-Z_]*__").search(attribute)]
    return normal_attributes

