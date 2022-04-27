# ____ ? _______ ?
#
#
# ___ test_get_duplicate_indices_docstring
#     words =  'is', 'it', 'true', 'or', 'is', 'it', 'not'
#     ... ? ? __ 0, 1
#
#
# ___ test_get_duplicate_indices_bite_text
#     words =  'this', 'is', 'a', 'new', 'bite', 'I', 'hope', 'this',
#              'bite', 'will', 'teach', 'you', 'something', 'new'
#     ... ? ? __ 0, 3, 4
#
#
# ___ test_get_duplicate_indices_another_text
#     # keeping it simple with split on space, so lists != lists.
#     words 'List comprehensions provide a concise way to create '
#              'lists. Common applications are to make new lists where '
#              'each element is the result of some operations applied '
#              'to each member of another sequence or iterable, or to '
#              'create a subsequence of those elements that satisfy a '
#              'certain condition' .s..
#     ... ? ? __ 3, 6, 7, 17, 22, 32