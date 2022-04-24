# ____ t___ _______ T..
# ____ c.. _______ C..
# _______ __
# _______ p.... __ pd
#
#
# ___ max_letter_word text s.. __ T.. s.., s.., i..
#     __ text __ [N.., T.., 1, 1.0, # list, dict
#         r.. V...
#     text ?.r.. '_', '' .r.. '--', '' .r.. '-', 'placeholder' .r.. '\'', 'pxaceholder'
#     text __.s.. '\W', ' ' ? #remove not word characters
#     text __.s.. ' +'  ' ' ? #remove extra spaces
#     t ''.j.. s ___ ? __ ? __ n.. a__ ?.i.. ___ ? __ ? #remove digit words
#
#     words t.s..
#     df ?.D.. ? columns_ 'word'
#
#     __ ?.e.. __ T..
#         r.. '' '' 0
#
#     ? 'casefold'   ? 'word' .s...r.. 'placeholder', ''
#     ? 'casefold'   ? 'casefold' .s...r.. 'pxaceholder', ''
#     ? 'word'   ? 'word' .s...r.. 'placeholder', '-' .r.. 'pxaceholder', '\''
#
#     ? 'casefold'   ? ? 'casefold' .s...s...a.. b..
#     ? ?.d..
#     ? 'casefold'   ? 'casefold' .s...l..
#     ? 'casefold'   ? 'casefold' .s...r..('ß', 'ss')
#
#     l_column   # list
#     c_column    # list
#     ___ w __ ? 'casefold' :
#         ?.a.. C.. ? .m.. 0 0
#         ?.a.. C.. ?.m.. 0 1
#
#     l_column =  'e' __ x __ '-' ____ ? ___ ? __ ?
#
#     ? 'letter'  ?
#     ? 'count'   ?
#     ? ?.d..
#     ? ?.s.. by_'count' ascending_F..
#
#     output ? 'word' ,i.. 0 ? 'letter' i.. 0 ? 'count' i.. 0
#
#     __ ? __ 'wepxaceholderve', 'e', 4
#         ? 'we\'ve', 'e', 2
#
#     r.. ?