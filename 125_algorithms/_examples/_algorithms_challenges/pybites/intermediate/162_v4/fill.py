HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    value = str(value)
    return f'{fill_char * (column_length - len(value))}{value}'