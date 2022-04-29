# ___ split_words_and_quoted_text text
#     """Split string text by space unless it is
#        wrapped inside double quotes, returning a list
#        of the elements.
#
#        For example
#        if text =
#        'Should give "3 elements only"'
#
#        the resulting list would be:
#        ['Should', 'give', '3 elements only']
#     """
#     # assume only one double-quoted string
#     s1 ? |?.i.. '"'
#     tmp  ? ?.i.. '"' + 1|
#     s2 ? |?.i.. '"'
#     s3 ? ?.i.. '"' + 1|
#
#     result ?.s..
#     ?.a.. ?
#     ?.e.. ?.s..
#     r.. ?
