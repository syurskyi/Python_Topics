# ____ col.. ______ d_d_
# _punct _ '.,;?:'
# ___ _normalize fragment
#     fragment _ fragment.l..
#     w__ le. ? > 0 an. ? -1 __ _?
#         ? _ ? ;-1
#     w__ le. ? > 0 an. ? 0 __ _?
#         ? _ ?|1;
#     r_ ?
#
# ___ numwords text
#     '''
#     Return the number of unique words in a body of text.
#
#     Punctuation and word casing are ignored.
#     '''
#     words _ se. _normalize(fragment) ___ fragment __ ?.sp..
#     ?.di.. ""
#     r_ le. ?
#
# ___ wordcounts text
#     '''
#     Return dictionary mapping words to the number of occurences.
#
#     Case is ignored, so each key is the lowercase version of the word.
#     '''
#     counts _ d_d_ __.
#     ___ fragment __ t__.sp..
#         word _ _n.. ?
#         __ ? __ '':
#             c___
#         c.. ? +_ 1
#     r_ di.. ?
#
# ___ addcounts existing, new
#     '''
#     Updates an existing word count dictionary, adding in new values.
#
#     Both existing and new are dicts that map words to counts (ints) - as might
#     be returned by wordcounts().
#
#     existing is modified. For each key in new, if that key is in existing, add
#     the value in existing.  Else set the value (i.e. treat the count in
#     existing as if 0).
#
#     If either existing or new are not dictionaries, raise ValueError
#     '''
#     __ no. ty.. ? __ di..
#         r_ V.. 'existing must be a dictionary'
#     __ no. ty.. n.. __ di..
#         r_ V.. 'new must be a dictionary'
#     ___ word count __ n__.v_i..
#         newcount _ c.. + e__.g.. w.. 0
#         e.. w.. _ ?
