HTML_SPACE '&nbsp;'


___ prefill_with_character(value, column_length=4, fill_char=HTML_SPACE
    """Prepend value with fill_char for given column_length"""
    value s..(value)
    r.. f'{fill_char * (column_length - l..(value}{value}'