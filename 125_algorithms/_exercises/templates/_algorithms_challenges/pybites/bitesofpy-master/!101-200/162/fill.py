HTML_SPACE = '&nbsp;'


___ prefill_with_character(value, column_length=4, fill_char=HTML_SPACE
    """Prepend value with fill_char for given column_length"""
    r_ f'{fill_char * (column_length - le.(str(value)))}{value}'
