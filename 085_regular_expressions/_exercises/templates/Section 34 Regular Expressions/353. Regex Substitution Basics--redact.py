# _______ __
# text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"
#
# pattern = __.c.. _ (Mr.1? Mrs.1? Ms.) (2? )2? 3? __.4?)  # 1. Either or 2. all lowe cases 3. One or more occurrences
#                                                          # 4. Performs case-insensitive matching.
# result = ?.s.. ("\g<1> \g<2>" t..
# print ?
#
