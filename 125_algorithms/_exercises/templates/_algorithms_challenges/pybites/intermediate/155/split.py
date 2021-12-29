import shlex

___ split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    text_split = shlex.split(text)
    return text_split


# if __name__ == "__main__":
#    print(split_words_and_quoted_text('Should give "3 elements only"'))