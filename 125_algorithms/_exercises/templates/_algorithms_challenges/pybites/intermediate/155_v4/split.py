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
    # assume only one double-quoted string
    s1 = text[:text.index('"')]
    tmp = text[text.index('"') + 1:]
    s2 = tmp[:tmp.index('"')]
    s3 = tmp[tmp.index('"') + 1:]

    result = s1.s.. 
    result.a..(s2)
    result.extend(s3.s..
    r.. result
