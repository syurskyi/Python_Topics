# ________ __
#
#
# ___ is_filename_safe filename
#     regex = 1? |2?||3?|*(4? jpg 5?  4? jpeg 5? 4? png 5? 4? gif 6?'  # 1. Starts with 2. all lower case letter, all upper case letter, all numbers
#                                                                  # 3. all lower case letter, all upper case letter, all numbers for any number of times
#                                                                  # 4. ekranirovanaja tochka
#                                                                  # 5. either or
#                                                                  # 6. end with
#     # ^[a-zA-Z0-9]          start with a-zA-Z0-9
#     # [a-zA-Z0-9_()-]+      then only contains a-zA-Z0-9_()- for any number of times
#     # (\.jpg|\.jpeg|\.png|\.gif)$       at last, it must end with one of the four extensions, remember to escape the dot
#     # since we check from start to end, it can either match the whole string or none
#     r_ __.m.. ? ? i. no. N..