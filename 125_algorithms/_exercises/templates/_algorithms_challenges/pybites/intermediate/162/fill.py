HTML_SPACE = '&nbsp;'


___ prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    value = str(value)
    __ l..(value) __ column_length:
        r.. value
    ____:
        delta = column_length - l..(value)
        r.. f"{fill_char * delta}{value}"


# if __name__ == "__main__":
#     print(prefill_with_character("1"))
#     print(prefill_with_character("20"))
#     print(prefill_with_character("315"))
#     print(prefill_with_character("1239"))