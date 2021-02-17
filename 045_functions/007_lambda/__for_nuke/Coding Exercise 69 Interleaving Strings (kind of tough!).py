# Interleaving Strings Solution
#
# Here's a detailed walkthrough.  I know it can be overwhelming,
# but try to step through one piece at a time if you get stuck.
#
#     I start by defining interleave , which accepts 2 strings: str1, and str2
#
#     To make this easier, let's use an example. Let's say that I call interleave('hi', 'no')
#
#     Focus on the innermost bit first. I zip the two strings together, w
#     hich returns a list of tuples like: [('h','n'), ('i','o')]
#
#     To get it back into a string, I need to:
#
#         First join the individual tuples into strings, which is what the first join() does
#
#             it results in a list of strings: ['hn', 'io']
#
#         Finally, join all the remaining strings into one large string
#
#             results in 'hnio'
#
#         Return the result!


def interleave(str1, str2):
    return ''.join(''.join(x) for x in (zip(str1, str2)))
