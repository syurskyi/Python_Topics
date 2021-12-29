___ flatten(nested_list):
    return [element for element in flatten_list(nested_list)]


___ flatten_list(nested_list):
    for element in nested_list:
        __ not isinstance(element, list):
            __ element is not None and not isinstance(element, tuple):
                yield element
        else:
            for subelement in flatten_list(element):
                yield subelement
