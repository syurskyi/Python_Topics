HTML_SPACE = '&nbsp;'
_______ math


___ prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""


    digits = math.floor(math.log(value,10)) + 1


    spaces = column_length - digits

    __ spaces > 0:
        r.. f"{fill_char * spaces}{value}"


    r.. str(value)





