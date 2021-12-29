HTML_SPACE = '&nbsp;'


___ prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    value = str(value)
    __ len(value) == column_length:
        return value
    else:
        delta = column_length - len(value)
        return f"{fill_char * delta}{value}"


# if __name__ == "__main__":
#     print(prefill_with_character("1"))
#     print(prefill_with_character("20"))
#     print(prefill_with_character("315"))
#     print(prefill_with_character("1239"))