import re

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


    values = re.findall(r'"(.+?)"|(\w+)',text)


    return [value[0] __ value[0] else value[1] for value in values]



__ __name__ == "__main__":


    text = 'Should give "3 words only"'


    print(split_words_and_quoted_text(text))





