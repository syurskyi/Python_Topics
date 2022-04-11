_______ __

___ split_words_and_quoted_text(text
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """


    values __.f..(r'"(.+?)"|(\w+)',text)


    r.. [value[0] __ value[0] ____ value[1] ___ value __ values]



__ _______ __ _______


    text 'Should give "3 words only"'


    print(split_words_and_quoted_text(text





